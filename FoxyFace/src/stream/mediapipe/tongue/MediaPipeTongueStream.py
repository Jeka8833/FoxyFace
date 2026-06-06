import ctypes
import logging
import logging.handlers
import multiprocessing as mp
import queue
from threading import Event, Thread

import numpy as np

from src.stream.core.StreamReadOnly import StreamReadOnly
from src.stream.core.StreamWriteOnly import StreamWriteOnly
from src.stream.core.components.WriteStreamSplitter import WriteStreamSplitter
from src.stream.mediapipe.tongue.MediaPipeTongueBlendShapeEnum import MediaPipeTongueBlendShapeEnum
from src.stream.mediapipe.tongue.MediaPipeTongueProcess import _onnx_worker_loop, IMAGE_SIZE, IMAGE_SHAPE, Status
from src.stream.postprocessing.frames.BlendShapesFrame import BlendShapesFrame
from src.stream.postprocessing.frames.ImageFrame import ImageFrame

_logger = logging.getLogger(__name__)


class MediaPipeTongueStream:
    def __init__(self, image_stream: StreamReadOnly[ImageFrame], frame_timeout: float | None):
        self.__image_stream = image_stream
        self.__frame_timeout = frame_timeout
        self.__stream_root = WriteStreamSplitter[BlendShapesFrame[MediaPipeTongueBlendShapeEnum]]()

        self.__ctx = mp.get_context("spawn")
        self.__worker = None
        self.__model_params = None

        self.__frame_timestamp = self.__ctx.Value(ctypes.c_longlong, 0, lock=False)
        self.__frame_image = self.__ctx.Array(ctypes.c_uint8, IMAGE_SIZE, lock=False)

        self.__cmd_queue = None
        self.__output_queue = None
        self.__frame_condition = None
        self.__model_run_status = None

        self.__close_event = Event()

        self.__log_queue = self.__ctx.Queue()

        root_logger = logging.getLogger()
        self.__log_listener = logging.handlers.QueueListener(
            self.__log_queue, *root_logger.handlers, respect_handler_level=True
        )
        self.__log_listener.start()

        self.__start_worker()

        self.__image_thread = Thread(target=self.__read_images_loop, daemon=True, name="MediaPipe Tongue Image Thread")
        self.__result_thread = Thread(target=self.__read_results_loop, daemon=True,
                                      name="MediaPipe Tongue Result Thread")
        self.__image_thread.start()
        self.__result_thread.start()
        self.__good_started = False

    def register_stream(self, stream: StreamWriteOnly[BlendShapesFrame[MediaPipeTongueBlendShapeEnum]]) -> None:
        self.__stream_root.register_stream(stream)

    def unregister_stream(self, stream: StreamWriteOnly[BlendShapesFrame[MediaPipeTongueBlendShapeEnum]]) -> None:
        self.__stream_root.unregister_stream(stream)

    @property
    def process_status(self) -> Status:
        status = self.__model_run_status
        if status is None:
            return Status.NOT_LOADED

        return Status(status.value)

    def load_model(self, provider_name: str | None, intra_op_num_threads: int, allow_spinning: bool,
                   device_id: int) -> None:
        self.__model_params = (provider_name, intra_op_num_threads, allow_spinning, device_id)
        self.__send_cmd("load_model", *self.__model_params)

    def __send_cmd(self, *cmd):
        cmd_q = self.__cmd_queue

        if cmd_q is None:
            return

        try:
            cmd_q.put(cmd)
        except Exception as e:
            _logger.warning(f"Failed to send command '{cmd[0]}': {e}")

    @staticmethod
    def __terminate_worker(worker):
        if worker is None or not worker.is_alive():
            return

        worker.terminate()
        worker.join(0.5)

        if worker.is_alive():
            worker.kill()
            worker.join()

    @staticmethod
    def __close_queues(*queues):
        for q in queues:
            if q is not None:
                try:
                    q.close()
                except Exception:
                    pass

    def __start_worker(self):
        self.__terminate_worker(self.__worker)
        self.__close_queues(self.__cmd_queue, self.__output_queue)

        self.__cmd_queue = self.__ctx.Queue()
        self.__output_queue = self.__ctx.Queue()
        self.__frame_condition = self.__ctx.Condition()
        self.__model_run_status = self.__ctx.Value(ctypes.c_uint8, 0)

        self.__worker = self.__ctx.Process(
            target=_onnx_worker_loop,
            args=(self.__log_queue, self.__cmd_queue, self.__output_queue,
                  self.__frame_timestamp, self.__frame_image, self.__frame_condition, self.__model_run_status),
            daemon=True,
            name="MediaPipeTongueWorker"
        )
        self.__worker.start()

    def close(self):
        self.__close_event.set()

        self.__send_cmd("stop")

        self.__stream_root.close()

        timeout = 5.0 if self.__frame_timeout is None else self.__frame_timeout * 2.0
        try:
            self.__image_thread.join(timeout)
            self.__result_thread.join(timeout)
        except Exception:
            pass

        self.__terminate_worker(self.__worker)

        if self.__log_listener is not None:
            self.__log_listener.stop()

        self.__close_queues(self.__cmd_queue, self.__output_queue, self.__log_queue)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __read_images_loop(self):
        while not self.__close_event.is_set():
            try:
                if self.__worker is None or not self.__worker.is_alive():
                    _logger.warning("MediaPipeTongueWorker died. Restarting and recovering state...")

                    self.__start_worker()

                    if self.__model_params is not None:
                        self.__send_cmd("load_model", *self.__model_params)

                last_frame = self.__image_stream.poll(self.__frame_timeout)
                if last_frame is None or last_frame.image is None:
                    continue

                img = last_frame.image

                if img.shape != IMAGE_SHAPE:
                    _logger.error(f"Image shape mismatch! Expected {IMAGE_SHAPE}, got {img.shape}")
                    continue

                if self.__frame_condition.acquire(timeout=0.05):
                    try:
                        dest = np.frombuffer(self.__frame_image, dtype=np.uint8).reshape(IMAGE_SHAPE)
                        np.copyto(dest, img)

                        self.__frame_timestamp.value = last_frame.timestamp_ns

                        self.__frame_condition.notify()
                    finally:
                        self.__frame_condition.release()
            except TimeoutError:
                continue
            except InterruptedError:
                return
            except Exception as e:
                _logger.warning(f"Exception in MediaPipe Tongue image loop: {e}", exc_info=True)

                self.__close_event.wait(0.005)

    def __read_results_loop(self):
        while not self.__close_event.is_set():
            try:
                timestamp, tongue_out = self.__output_queue.get(timeout=0.05)

                self.__stream_root.put(BlendShapesFrame(
                    {MediaPipeTongueBlendShapeEnum.TongueOut: tongue_out},
                    timestamp)
                )
                self.__good_started = True
            except queue.Empty:
                continue
            except (ValueError, OSError):
                self.__close_event.wait(0.05)
            except Exception as e:
                _logger.warning(f"Exception in MediaPipe Tongue result loop: {e}", exc_info=True)

                self.__close_event.wait(0.005)
