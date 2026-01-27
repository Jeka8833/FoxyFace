from blendshape_router.preset.ARKitParameter import ARKitParameter
from blendshape_router.preset.BaseParameter import BaseParameter
from blendshape_router.preset.EyeCalculations import EyeCalculations
from scipy.spatial.transform import Rotation

from stream.postprocessing.GeneralBlendShapeEnum import GeneralBlendShapeEnum


class GeneralToBlendshapeRouterMapper:

    @staticmethod
    def convert(general_values: dict[GeneralBlendShapeEnum, float | Rotation]) -> dict[
        BaseParameter | ARKitParameter, float | Rotation]:
        return {

            BaseParameter.CheekPuffLeft: general_values.get(GeneralBlendShapeEnum.CheekPuffLeft,
                                                            general_values.get(GeneralBlendShapeEnum.CheekPuff)),
            BaseParameter.CheekPuffRight: general_values.get(GeneralBlendShapeEnum.CheekPuffRight,
                                                             general_values.get(GeneralBlendShapeEnum.CheekPuff)),
            BaseParameter.CheekSuckLeft: general_values.get(GeneralBlendShapeEnum.CheekSuckLeft),
            BaseParameter.CheekSuckRight: general_values.get(GeneralBlendShapeEnum.CheekSuckRight),
            ARKitParameter.JawOpen: general_values.get(GeneralBlendShapeEnum.JawOpen),
            ARKitParameter.JawForward: general_values.get(GeneralBlendShapeEnum.JawForward),
            ARKitParameter.JawLeft: general_values.get(GeneralBlendShapeEnum.JawLeft),
            ARKitParameter.JawRight: general_values.get(GeneralBlendShapeEnum.JawRight),
            ARKitParameter.NoseSneerLeft: general_values.get(GeneralBlendShapeEnum.NoseSneerLeft),
            ARKitParameter.NoseSneerRight: general_values.get(GeneralBlendShapeEnum.NoseSneerRight),
            ARKitParameter.MouthFunnel: general_values.get(GeneralBlendShapeEnum.MouthFunnel),
            ARKitParameter.MouthPucker: general_values.get(GeneralBlendShapeEnum.MouthPucker),
            ARKitParameter.MouthLeft: general_values.get(GeneralBlendShapeEnum.MouthLeft),
            ARKitParameter.MouthRight: general_values.get(GeneralBlendShapeEnum.MouthRight),
            ARKitParameter.MouthRollUpper: general_values.get(GeneralBlendShapeEnum.MouthRollUpper),
            ARKitParameter.MouthRollLower: general_values.get(GeneralBlendShapeEnum.MouthRollLower),
            ARKitParameter.MouthShrugUpper: general_values.get(GeneralBlendShapeEnum.MouthRaiserUpper),
            ARKitParameter.MouthShrugLower: general_values.get(GeneralBlendShapeEnum.MouthRaiserLower),
            ARKitParameter.MouthClose: general_values.get(GeneralBlendShapeEnum.MouthClosed),
            ARKitParameter.MouthSmileLeft: general_values.get(GeneralBlendShapeEnum.MouthSmileLeft),
            ARKitParameter.MouthSmileRight: general_values.get(GeneralBlendShapeEnum.MouthSmileRight),
            ARKitParameter.MouthFrownLeft: general_values.get(GeneralBlendShapeEnum.MouthFrownLeft),
            ARKitParameter.MouthFrownRight: general_values.get(GeneralBlendShapeEnum.MouthFrownRight),
            ARKitParameter.MouthDimpleLeft: general_values.get(GeneralBlendShapeEnum.MouthDimpleLeft),
            ARKitParameter.MouthDimpleRight: general_values.get(GeneralBlendShapeEnum.MouthDimpleRight),
            ARKitParameter.MouthUpperUpLeft: general_values.get(GeneralBlendShapeEnum.MouthUpperUpLeft),
            ARKitParameter.MouthUpperUpRight: general_values.get(GeneralBlendShapeEnum.MouthUpperUpRight),
            ARKitParameter.MouthLowerDownLeft: general_values.get(GeneralBlendShapeEnum.MouthLowerDownLeft),
            ARKitParameter.MouthLowerDownRight: general_values.get(GeneralBlendShapeEnum.MouthLowerDownRight),
            ARKitParameter.MouthPressLeft: general_values.get(GeneralBlendShapeEnum.MouthPressLeft),
            ARKitParameter.MouthPressRight: general_values.get(GeneralBlendShapeEnum.MouthPressRight),
            ARKitParameter.MouthStretchLeft: general_values.get(GeneralBlendShapeEnum.MouthStretchLeft),
            ARKitParameter.MouthStretchRight: general_values.get(GeneralBlendShapeEnum.MouthStretchRight),
            ARKitParameter.TongueOut: general_values.get(GeneralBlendShapeEnum.TongueOut),
            BaseParameter.TongueUp: general_values.get(GeneralBlendShapeEnum.TongueUp),
            BaseParameter.TongueDown: general_values.get(GeneralBlendShapeEnum.TongueDown),
            BaseParameter.TongueLeft: general_values.get(GeneralBlendShapeEnum.TongueLeft),
            BaseParameter.TongueRight: general_values.get(GeneralBlendShapeEnum.TongueRight),
            BaseParameter.TongueRoll: general_values.get(GeneralBlendShapeEnum.TongueRoll),
            BaseParameter.TongueBendDown: general_values.get(GeneralBlendShapeEnum.TongueBendDown),
            BaseParameter.TongueCurlUp: general_values.get(GeneralBlendShapeEnum.TongueCurlUp),
            BaseParameter.TongueSquish: general_values.get(GeneralBlendShapeEnum.TongueSquish),
            BaseParameter.TongueFlat: general_values.get(GeneralBlendShapeEnum.TongueFlat),
            BaseParameter.TongueTwistLeft: general_values.get(GeneralBlendShapeEnum.TongueTwistLeft),
            BaseParameter.TongueTwistRight: general_values.get(GeneralBlendShapeEnum.TongueTwistRight),
            ARKitParameter.BrowDownLeft: general_values.get(GeneralBlendShapeEnum.BrowDownLeft),
            ARKitParameter.BrowDownRight: general_values.get(GeneralBlendShapeEnum.BrowDownRight),
            ARKitParameter.BrowInnerUpLeft: general_values.get(GeneralBlendShapeEnum.BrowInnerUp),
            ARKitParameter.BrowInnerUpRight: general_values.get(GeneralBlendShapeEnum.BrowInnerUp),
            ARKitParameter.BrowOuterUpLeft: general_values.get(GeneralBlendShapeEnum.BrowOuterUpLeft),
            ARKitParameter.BrowOuterUpRight: general_values.get(GeneralBlendShapeEnum.BrowOuterUpRight),
            ARKitParameter.CheekSquintLeft: general_values.get(GeneralBlendShapeEnum.CheekSquintLeft),
            ARKitParameter.CheekSquintRight: general_values.get(GeneralBlendShapeEnum.CheekSquintRight),
            ARKitParameter.EyeBlinkLeft: general_values.get(GeneralBlendShapeEnum.EyeBlinkLeft),
            ARKitParameter.EyeBlinkRight: general_values.get(GeneralBlendShapeEnum.EyeBlinkRight),
            ARKitParameter.EyeLookDownLeft: general_values.get(GeneralBlendShapeEnum.EyeLookDownLeft),
            ARKitParameter.EyeLookDownRight: general_values.get(GeneralBlendShapeEnum.EyeLookDownRight),
            ARKitParameter.EyeLookInLeft: general_values.get(GeneralBlendShapeEnum.EyeLookInLeft),
            ARKitParameter.EyeLookInRight: general_values.get(GeneralBlendShapeEnum.EyeLookInRight),
            ARKitParameter.EyeLookOutLeft: general_values.get(GeneralBlendShapeEnum.EyeLookOutLeft),
            ARKitParameter.EyeLookOutRight: general_values.get(GeneralBlendShapeEnum.EyeLookOutRight),
            ARKitParameter.EyeLookUpLeft: general_values.get(GeneralBlendShapeEnum.EyeLookUpLeft),
            ARKitParameter.EyeLookUpRight: general_values.get(GeneralBlendShapeEnum.EyeLookUpRight),
            ARKitParameter.EyeSquintLeft: general_values.get(GeneralBlendShapeEnum.EyeSquintLeft),
            ARKitParameter.EyeSquintRight: general_values.get(GeneralBlendShapeEnum.EyeSquintRight),
            ARKitParameter.EyeWideLeft: general_values.get(GeneralBlendShapeEnum.EyeWideLeft),
            ARKitParameter.EyeWideRight: general_values.get(GeneralBlendShapeEnum.EyeWideRight),
            ARKitParameter.TransformTranslationX: general_values.get(GeneralBlendShapeEnum.HeadX),
            ARKitParameter.TransformTranslationY: general_values.get(GeneralBlendShapeEnum.HeadY),
            ARKitParameter.TransformTranslationZ: general_values.get(GeneralBlendShapeEnum.HeadZ),
            ARKitParameter.TransformRotation: general_values.get(GeneralBlendShapeEnum.HeadRotation),
            ARKitParameter.LeftEyeRotation: GeneralToBlendshapeRouterMapper.__eye_rotation_value(
                general_values.get(GeneralBlendShapeEnum.EyeLookOutLeft),
                general_values.get(GeneralBlendShapeEnum.EyeLookInLeft),
                general_values.get(GeneralBlendShapeEnum.EyeLookDownLeft),
                general_values.get(GeneralBlendShapeEnum.EyeLookUpLeft)),
            ARKitParameter.RightEyeRotation: GeneralToBlendshapeRouterMapper.__eye_rotation_value(
                general_values.get(GeneralBlendShapeEnum.EyeLookInRight),
                general_values.get(GeneralBlendShapeEnum.EyeLookOutRight),
                general_values.get(GeneralBlendShapeEnum.EyeLookDownRight),
                general_values.get(GeneralBlendShapeEnum.EyeLookUpRight)),

        }

    @staticmethod
    def __eye_rotation_value(x_negative: float | None, x_positive: float | None, y_negative: float | None,
                             y_positive: float | None) -> Rotation | None:
        x: float | None = None if x_negative is None and x_positive is None else (
                (x_positive or 0.0) - (x_negative or 0.0))
        y: float | None = None if y_negative is None and y_positive is None else (
                (y_positive or 0.0) - (y_negative or 0.0))

        if x is None and y is None:
            return None

        return EyeCalculations.shift_to_rotation(x or 0.0, y or 0.0)
