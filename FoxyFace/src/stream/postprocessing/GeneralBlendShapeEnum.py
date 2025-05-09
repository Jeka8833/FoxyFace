from enum import Enum, unique

from src.stream.babble.BabbleBlendShapeEnum import BabbleBlendShapeEnum
from src.stream.mediapipe.MediaPipeBlendShapeEnum import MediaPipeBlendShapeEnum
from src.stream.postprocessing.GeneralBlendShapeOption import GeneralBlendShapeOption


@unique
class GeneralBlendShapeEnum(Enum):
    # Babble + MediaPipe
    CheekPuffLeft = GeneralBlendShapeOption(same_as=[BabbleBlendShapeEnum.CheekPuffLeft])
    CheekPuffRight = GeneralBlendShapeOption(same_as=[BabbleBlendShapeEnum.CheekPuffRight])
    CheekSuckLeft = GeneralBlendShapeOption(same_as=[BabbleBlendShapeEnum.CheekSuckLeft])
    CheekSuckRight = GeneralBlendShapeOption(same_as=[BabbleBlendShapeEnum.CheekSuckRight])
    JawOpen = GeneralBlendShapeOption(same_as=[MediaPipeBlendShapeEnum.JawOpen, BabbleBlendShapeEnum.JawOpen])
    JawForward = GeneralBlendShapeOption(same_as=[MediaPipeBlendShapeEnum.JawForward, BabbleBlendShapeEnum.JawForward])
    JawLeft = GeneralBlendShapeOption(same_as=[MediaPipeBlendShapeEnum.JawLeft, BabbleBlendShapeEnum.JawLeft])
    JawRight = GeneralBlendShapeOption(same_as=[MediaPipeBlendShapeEnum.JawRight, BabbleBlendShapeEnum.JawRight])
    NoseSneerLeft = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendShapeEnum.NoseSneerLeft, BabbleBlendShapeEnum.NoseSneerLeft])
    NoseSneerRight = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendShapeEnum.NoseSneerRight, BabbleBlendShapeEnum.NoseSneerRight])
    MouthFunnel = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendShapeEnum.MouthFunnel, BabbleBlendShapeEnum.MouthFunnel])
    MouthPucker = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendShapeEnum.MouthPucker, BabbleBlendShapeEnum.MouthPucker])
    MouthLeft = GeneralBlendShapeOption(same_as=[MediaPipeBlendShapeEnum.MouthLeft, BabbleBlendShapeEnum.MouthLeft])
    MouthRight = GeneralBlendShapeOption(same_as=[MediaPipeBlendShapeEnum.MouthRight, BabbleBlendShapeEnum.MouthRight])
    MouthRollUpper = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendShapeEnum.MouthRollUpper, BabbleBlendShapeEnum.MouthRollUpper])
    MouthRollLower = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendShapeEnum.MouthRollLower, BabbleBlendShapeEnum.MouthRollLower])
    MouthRaiserUpper = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendShapeEnum.MouthShrugUpper, BabbleBlendShapeEnum.MouthRaiserUpper])
    MouthRaiserLower = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendShapeEnum.MouthShrugLower, BabbleBlendShapeEnum.MouthRaiserLower])
    MouthClosed = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendShapeEnum.MouthClose, BabbleBlendShapeEnum.MouthClosed])
    MouthSmileLeft = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendShapeEnum.MouthSmileLeft, BabbleBlendShapeEnum.MouthSmileLeft])
    MouthSmileRight = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendShapeEnum.MouthSmileRight, BabbleBlendShapeEnum.MouthSmileRight])
    MouthFrownLeft = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendShapeEnum.MouthFrownLeft, BabbleBlendShapeEnum.MouthFrownLeft])
    MouthFrownRight = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendShapeEnum.MouthFrownRight, BabbleBlendShapeEnum.MouthFrownRight])
    MouthDimpleLeft = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendShapeEnum.MouthDimpleLeft, BabbleBlendShapeEnum.MouthDimpleLeft])
    MouthDimpleRight = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendShapeEnum.MouthDimpleRight, BabbleBlendShapeEnum.MouthDimpleRight])
    MouthUpperUpLeft = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendShapeEnum.MouthUpperUpLeft, BabbleBlendShapeEnum.MouthUpperUpLeft])
    MouthUpperUpRight = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendShapeEnum.MouthUpperUpRight, BabbleBlendShapeEnum.MouthUpperUpRight])
    MouthLowerDownLeft = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendShapeEnum.MouthLowerDownLeft, BabbleBlendShapeEnum.MouthLowerDownLeft])
    MouthLowerDownRight = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendShapeEnum.MouthLowerDownRight, BabbleBlendShapeEnum.MouthLowerDownRight])
    MouthPressLeft = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendShapeEnum.MouthPressLeft, BabbleBlendShapeEnum.MouthPressLeft])
    MouthPressRight = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendShapeEnum.MouthPressRight, BabbleBlendShapeEnum.MouthPressRight])
    MouthStretchLeft = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendShapeEnum.MouthStretchLeft, BabbleBlendShapeEnum.MouthStretchLeft])
    MouthStretchRight = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendShapeEnum.MouthStretchRight, BabbleBlendShapeEnum.MouthStretchRight])
    TongueOut = GeneralBlendShapeOption(same_as=[BabbleBlendShapeEnum.TongueOut])
    TongueUp = GeneralBlendShapeOption(same_as=[BabbleBlendShapeEnum.TongueUp])
    TongueDown = GeneralBlendShapeOption(same_as=[BabbleBlendShapeEnum.TongueDown])
    TongueLeft = GeneralBlendShapeOption(same_as=[BabbleBlendShapeEnum.TongueLeft])
    TongueRight = GeneralBlendShapeOption(same_as=[BabbleBlendShapeEnum.TongueRight])
    TongueRoll = GeneralBlendShapeOption(same_as=[BabbleBlendShapeEnum.TongueRoll])
    TongueBendDown = GeneralBlendShapeOption(same_as=[BabbleBlendShapeEnum.TongueBendDown])
    TongueCurlUp = GeneralBlendShapeOption(same_as=[BabbleBlendShapeEnum.TongueCurlUp])
    TongueSquish = GeneralBlendShapeOption(same_as=[BabbleBlendShapeEnum.TongueSquish])
    TongueFlat = GeneralBlendShapeOption(same_as=[BabbleBlendShapeEnum.TongueFlat])
    TongueTwistLeft = GeneralBlendShapeOption(same_as=[BabbleBlendShapeEnum.TongueTwistLeft])
    TongueTwistRight = GeneralBlendShapeOption(same_as=[BabbleBlendShapeEnum.TongueTwistRight])

    # MediaPipe
    BrowDownLeft = GeneralBlendShapeOption(same_as=[MediaPipeBlendShapeEnum.BrowDownLeft])
    BrowDownRight = GeneralBlendShapeOption(same_as=[MediaPipeBlendShapeEnum.BrowDownRight])
    BrowInnerUp = GeneralBlendShapeOption(same_as=[MediaPipeBlendShapeEnum.BrowInnerUp])
    BrowOuterUpLeft = GeneralBlendShapeOption(same_as=[MediaPipeBlendShapeEnum.BrowOuterUpLeft])
    BrowOuterUpRight = GeneralBlendShapeOption(same_as=[MediaPipeBlendShapeEnum.BrowOuterUpRight])
    CheekPuff = GeneralBlendShapeOption(same_as=[MediaPipeBlendShapeEnum.CheekPuff])
    CheekSquintLeft = GeneralBlendShapeOption(same_as=[MediaPipeBlendShapeEnum.CheekSquintLeft])
    CheekSquintRight = GeneralBlendShapeOption(same_as=[MediaPipeBlendShapeEnum.CheekSquintRight])
    EyeBlinkLeft = GeneralBlendShapeOption(same_as=[MediaPipeBlendShapeEnum.EyeBlinkLeft])
    EyeBlinkRight = GeneralBlendShapeOption(same_as=[MediaPipeBlendShapeEnum.EyeBlinkRight])
    EyeSquintLeft = GeneralBlendShapeOption(same_as=[MediaPipeBlendShapeEnum.EyeSquintLeft])
    EyeSquintRight = GeneralBlendShapeOption(same_as=[MediaPipeBlendShapeEnum.EyeSquintRight])
    EyeWideLeft = GeneralBlendShapeOption(same_as=[MediaPipeBlendShapeEnum.EyeWideLeft])
    EyeWideRight = GeneralBlendShapeOption(same_as=[MediaPipeBlendShapeEnum.EyeWideRight])
    EyeXLeft = GeneralBlendShapeOption(same_as=[MediaPipeBlendShapeEnum.EyeXLeft], min_value=-1.0, has_center=True)
    EyeXRight = GeneralBlendShapeOption(same_as=[MediaPipeBlendShapeEnum.EyeXRight], min_value=-1.0, has_center=True)
    EyeYLeft = GeneralBlendShapeOption(same_as=[MediaPipeBlendShapeEnum.EyeYLeft], min_value=-1.0, has_center=True)
    EyeYRight = GeneralBlendShapeOption(same_as=[MediaPipeBlendShapeEnum.EyeYRight], min_value=-1.0, has_center=True)
    HeadX = GeneralBlendShapeOption(same_as=[MediaPipeBlendShapeEnum.HeadX], min_value=-1.0, has_center=True)
    HeadY = GeneralBlendShapeOption(same_as=[MediaPipeBlendShapeEnum.HeadY], min_value=-1.0, has_center=True)
    HeadZ = GeneralBlendShapeOption(same_as=[MediaPipeBlendShapeEnum.HeadZ], min_value=-1.0, has_center=True)
    HeadPitch = GeneralBlendShapeOption(same_as=[MediaPipeBlendShapeEnum.HeadPitch], min_value=-1.0, has_center=True,
                                        disable_calibration=True)
    HeadYaw = GeneralBlendShapeOption(same_as=[MediaPipeBlendShapeEnum.HeadYaw], min_value=-1.0, has_center=True,
                                      disable_calibration=True)
    HeadRoll = GeneralBlendShapeOption(same_as=[MediaPipeBlendShapeEnum.HeadRoll], min_value=-1.0, has_center=True,
                                       disable_calibration=True)
