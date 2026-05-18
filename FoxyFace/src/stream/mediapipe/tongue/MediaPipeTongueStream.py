import logging
from pathlib import Path
from threading import Event, Thread

from src.stream.core.StreamReadOnly import StreamReadOnly
from src.stream.core.StreamWriteOnly import StreamWriteOnly
from src.stream.core.components.WriteStreamSplitter import WriteStreamSplitter
from src.stream.mediapipe.face.core.MediaPipeFrame import MediaPipeFrame
from src.stream.mediapipe.tongue.MediaPipeTongueBlendShapeEnum import MediaPipeTongueBlendShapeEnum
from src.stream.postprocessing.BlendShapesFrame import BlendShapesFrame

_logger = logging.getLogger(__name__)

class MediaPipeTongueStream:
    def __init__(self, image_stream: StreamReadOnly[MediaPipeFrame], model_path: Path,
                 frame_timeout: float | None):
        self.__image_stream: StreamReadOnly[MediaPipeFrame] = image_stream
        self.__frame_timeout: float | None = frame_timeout

        self.__stream_root = WriteStreamSplitter[BlendShapesFrame[MediaPipeTongueBlendShapeEnum]]()

        self.__close_event = Event()

        self.__thread = Thread(target=self.__loop, daemon=True, name="MediaPipe Tongue Thread")
        self.__thread.start()

    def register_stream(self, stream: StreamWriteOnly[BlendShapesFrame[MediaPipeTongueBlendShapeEnum]]) -> None:
        self.__stream_root.register_stream(stream)

    def unregister_stream(self, stream: StreamWriteOnly[BlendShapesFrame[MediaPipeTongueBlendShapeEnum]]) -> None:
        self.__stream_root.unregister_stream(stream)

    def close(self):
        self.__close_event.set()
        self.__stream_root.close()

        try:
            if self.__frame_timeout is None:
                self.__thread.join(5.0)
            else:
                self.__thread.join(self.__frame_timeout * 2.0)
        except Exception:
            _logger.warning("Failed to join MediaPipe thread", exc_info=True, stack_info=True)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __loop(self):
        while not self.__close_event.is_set():
            try:
                frame = self.__image_stream.poll(self.__frame_timeout)

            except TimeoutError:
                continue
            except InterruptedError:
                return
            except Exception:
                _logger.warning("Exception in MediaPipe loop", exc_info=True, stack_info=True)

                self.__close_event.wait(0.001)