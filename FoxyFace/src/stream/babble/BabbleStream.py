import logging
from threading import Event, Thread

from src.stream.babble.BabbleBlendShapeEnum import BabbleBlendShapeEnum
from src.stream.babble.BabbleModelLoader import BabbleModelLoader
from src.stream.babble.imageprocessing.BabbleImageFrame import BabbleImageFrame
from src.stream.core.StreamReadOnly import StreamReadOnly
from src.stream.core.StreamWriteOnly import StreamWriteOnly
from src.stream.core.components.WriteStreamSplitter import WriteStreamSplitter
from src.stream.postprocessing.BlendShapesFrame import BlendShapesFrame

_logger = logging.getLogger(__name__)


class BabbleStream:
    def __init__(self, stream: StreamReadOnly[BabbleImageFrame], frame_timeout: float | None, model: BabbleModelLoader):
        self.__babble_image_stream: StreamReadOnly[BabbleImageFrame] = stream
        self.__frame_timeout: float | None = frame_timeout
        self.__model = model

        self.__close_event = Event()

        self.__stream_root = WriteStreamSplitter[BlendShapesFrame[BabbleBlendShapeEnum]]()

        self.__thread = Thread(target=self.__loop, daemon=True, name="Babble Thread")
        self.__thread.start()

    def register_stream(self, stream: StreamWriteOnly[BlendShapesFrame[BabbleBlendShapeEnum]]) -> None:
        self.__stream_root.register_stream(stream)

    def unregister_stream(self, stream: StreamWriteOnly[BlendShapesFrame[BabbleBlendShapeEnum]]) -> None:
        self.__stream_root.unregister_stream(stream)

    def close(self):
        self.__close_event.set()
        self.__stream_root.close()

        self.__thread.join()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __loop(self):
        while not self.__close_event.is_set():
            try:
                last_frame = self.__babble_image_stream.poll(self.__frame_timeout)
                bend_shapes = self.__model.process_gray_image(last_frame.processed_frame)
                if bend_shapes is None:
                    continue

                self.__stream_root.put(BlendShapesFrame(bend_shapes, last_frame.timestamp_ns))
            except TimeoutError:
                continue
            except InterruptedError:
                return
            except Exception:
                _logger.warning("Exception in Babble loop", exc_info=True, stack_info=True)

                self.__close_event.wait(0.001)
