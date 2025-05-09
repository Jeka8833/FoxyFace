import numpy

from src.stream.core.StreamReadOnly import StreamReadOnly
from src.stream.postprocessing.BlendShapesFrame import BlendShapesFrame
from src.stream.postprocessing.GeneralBlendShapeEnum import GeneralBlendShapeEnum
from src.stream.postprocessing.calibration.CalibrateProcessingOptions import CalibrateProcessingOptions


class CalibrateProcessing(StreamReadOnly[BlendShapesFrame[GeneralBlendShapeEnum]]):
    def __init__(self, stream: StreamReadOnly[BlendShapesFrame[GeneralBlendShapeEnum]],
                 options: CalibrateProcessingOptions):
        self.__stream: StreamReadOnly[BlendShapesFrame[GeneralBlendShapeEnum]] = stream
        self.__options: CalibrateProcessingOptions = options

    def poll(self, timeout: float | None = None) -> BlendShapesFrame[GeneralBlendShapeEnum]:
        frame = self.__stream.poll(timeout)

        blend_shapes = frame.blend_shapes.copy()

        for key, value in frame.blend_shapes.items():
            if key.value.disable_calibration:
                continue

            try:
                option = self.__options.blend_shape_options.get(key)
                if option is not None:
                    if key.value.has_center:
                        x = (option.max_pose_negative, option.neutral_pose, option.max_pose_positive)
                        y = (key.value.min_value, 0.0, key.value.max_value)
                    else:
                        x = (option.neutral_pose, option.max_pose_positive)
                        y = (key.value.min_value, key.value.max_value)

                    blend_shapes[key] = float(numpy.interp(value, x, y))
            except Exception:
                pass

        return BlendShapesFrame(blend_shapes, frame.timestamp_ns)
