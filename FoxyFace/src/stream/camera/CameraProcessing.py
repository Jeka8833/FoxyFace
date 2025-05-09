import cv2

from src.stream.camera.CameraFrame import CameraFrame
from src.stream.camera.CameraProcessingOption import CameraProcessingOption
from src.stream.core.StreamReadOnly import StreamReadOnly


class CameraProcessing(StreamReadOnly[CameraFrame]):
    def __init__(self, stream: StreamReadOnly[CameraFrame], options: CameraProcessingOption):
        self.__stream: StreamReadOnly[CameraFrame] = stream
        self.__post_processing_options: CameraProcessingOption = options

    def poll(self, timeout: float | None = None) -> CameraFrame:
        packet = self.__stream.poll(timeout)

        new_frame = cv2.cvtColor(packet.frame, cv2.COLOR_BGR2RGB)

        # You can optimize flip and rotate to max two calls, if you need, im too lazy

        if self.__post_processing_options.mirror_x:
            new_frame = cv2.flip(new_frame, 1)
        if self.__post_processing_options.mirror_y:
            new_frame = cv2.flip(new_frame, 0)
        if self.__post_processing_options.rotate_ninety:
            new_frame = cv2.rotate(new_frame, cv2.ROTATE_90_CLOCKWISE)

        return CameraFrame(new_frame, packet.timestamp_ns)
