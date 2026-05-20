import cv2

from src.stream.camera.CameraProcessingOption import CameraProcessingOption
from src.stream.core.StreamReadOnly import StreamReadOnly
from src.stream.postprocessing.frames.ImageFrame import ImageFrame


class CameraProcessing(StreamReadOnly[ImageFrame]):
    def __init__(self, stream: StreamReadOnly[ImageFrame], options: CameraProcessingOption):
        self.__stream: StreamReadOnly[ImageFrame] = stream
        self.__post_processing_options: CameraProcessingOption = options

    def poll(self, timeout: float | None = None) -> ImageFrame:
        packet = self.__stream.poll(timeout)

        new_frame = cv2.cvtColor(packet.image, cv2.COLOR_BGR2RGB)

        # You can optimize flip and rotate to max two calls, if you need, im too lazy

        if self.__post_processing_options.mirror_x:
            new_frame = cv2.flip(new_frame, 1)
        if self.__post_processing_options.mirror_y:
            new_frame = cv2.flip(new_frame, 0)
        if self.__post_processing_options.rotate_ninety:
            new_frame = cv2.rotate(new_frame, cv2.ROTATE_90_CLOCKWISE)

        return ImageFrame(new_frame, packet.timestamp_ns)
