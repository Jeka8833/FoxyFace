import logging
from threading import Event, Thread

from src.stream.core.StreamReadOnly import StreamReadOnly
from src.stream.core.StreamWriteOnly import StreamWriteOnly
from src.stream.core.components.WriteStreamSplitter import WriteStreamSplitter
from src.stream.mediapipe.tongue.MediaPipeTongueBlendShapeEnum import MediaPipeTongueBlendShapeEnum
from src.stream.mediapipe.tongue.MediaPipeTongueModel import MediaPipeTongueModel
from src.stream.postprocessing.frames.BlendShapesFrame import BlendShapesFrame
from src.stream.postprocessing.frames.ImageFrame import ImageFrame

_logger = logging.getLogger(__name__)


class MediaPipeTongueStream:
    def __init__(self, image_stream: StreamReadOnly[ImageFrame], frame_timeout: float | None):
        self.__image_stream: StreamReadOnly[ImageFrame] = image_stream
        self.__frame_timeout: float | None = frame_timeout

        self.__stream_root = WriteStreamSplitter[BlendShapesFrame[MediaPipeTongueBlendShapeEnum]]()

        self.model: MediaPipeTongueModel | None = None

        self.__close_event = Event()

        self.__thread = Thread(target=self.__loop, daemon=True, name="MediaPipe Tongue Thread")
        self.__thread.start()

    def register_stream(self, stream: StreamWriteOnly[BlendShapesFrame[MediaPipeTongueBlendShapeEnum]]) -> None:
        self.__stream_root.register_stream(stream)

    def unregister_stream(self, stream: StreamWriteOnly[BlendShapesFrame[MediaPipeTongueBlendShapeEnum]]) -> None:
        self.__stream_root.unregister_stream(stream)

    @property
    def model(self) -> MediaPipeTongueModel | None:
        return self.__model

    @model.setter
    def model(self, model: MediaPipeTongueModel | None):
        if model is not None and not isinstance(model, MediaPipeTongueModel):
            raise TypeError("model isn't MediaPipeTongueModel")

        self.__model = model

    def close(self):
        self.__close_event.set()
        self.__stream_root.close()

        try:
            if self.__frame_timeout is None:
                self.__thread.join(5.0)
            else:
                self.__thread.join(self.__frame_timeout * 2.0)
        except Exception:
            _logger.warning("Failed to join MediaPipe Tongue thread", exc_info=True, stack_info=True)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __loop(self):
        while not self.__close_event.is_set():
            try:
                last_frame = self.__image_stream.poll(self.__frame_timeout)

                model = self.model
                if model is None:
                    continue

                tongue_out = model.run(last_frame.image)

                self.__stream_root.put(BlendShapesFrame(
                    {MediaPipeTongueBlendShapeEnum.TongueOut: tongue_out},
                    last_frame.timestamp_ns)
                )
            except TimeoutError:
                continue
            except InterruptedError:
                return
            except Exception:
                _logger.warning("Exception in MediaPipe Tongue loop", exc_info=True, stack_info=True)

                self.__close_event.wait(0.001)
