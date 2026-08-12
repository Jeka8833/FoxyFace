from enum import Enum, unique

from src.stream.babble.BabbleBlendshapeEnum import BabbleBlendshapeEnum
from src.stream.mediapipe.face.MediaPipeBlendshapeEnum import MediaPipeBlendshapeEnum
from src.stream.mediapipe.tongue.MediaPipeTongueBlendshapeEnum import MediaPipeTongueBlendshapeEnum
from src.stream.postprocessing.GeneralBlendShapeOption import GeneralBlendShapeOption


@unique
class GeneralBlendShapeEnum(Enum):
    # Babble + MediaPipe
    CheekPuffLeft = GeneralBlendShapeOption(same_as=[BabbleBlendshapeEnum.CheekPuffLeft])
    CheekPuffRight = GeneralBlendShapeOption(same_as=[BabbleBlendshapeEnum.CheekPuffRight])
    CheekSuckLeft = GeneralBlendShapeOption(same_as=[BabbleBlendshapeEnum.CheekSuckLeft])
    CheekSuckRight = GeneralBlendShapeOption(same_as=[BabbleBlendshapeEnum.CheekSuckRight])
    JawOpen = GeneralBlendShapeOption(same_as=[MediaPipeBlendshapeEnum.JawOpen, BabbleBlendshapeEnum.JawOpen])
    JawForward = GeneralBlendShapeOption(same_as=[MediaPipeBlendshapeEnum.JawForward, BabbleBlendshapeEnum.JawForward])
    JawLeft = GeneralBlendShapeOption(same_as=[MediaPipeBlendshapeEnum.JawLeft, BabbleBlendshapeEnum.JawLeft])
    JawRight = GeneralBlendShapeOption(same_as=[MediaPipeBlendshapeEnum.JawRight, BabbleBlendshapeEnum.JawRight])
    NoseSneerLeft = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendshapeEnum.NoseSneerLeft, BabbleBlendshapeEnum.NoseSneerLeft])
    NoseSneerRight = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendshapeEnum.NoseSneerRight, BabbleBlendshapeEnum.NoseSneerRight])
    MouthFunnel = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendshapeEnum.MouthFunnel, BabbleBlendshapeEnum.MouthFunnel])
    MouthPucker = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendshapeEnum.MouthPucker, BabbleBlendshapeEnum.MouthPucker])
    MouthLeft = GeneralBlendShapeOption(same_as=[MediaPipeBlendshapeEnum.MouthLeft, BabbleBlendshapeEnum.MouthLeft])
    MouthRight = GeneralBlendShapeOption(same_as=[MediaPipeBlendshapeEnum.MouthRight, BabbleBlendshapeEnum.MouthRight])
    MouthRollUpper = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendshapeEnum.MouthRollUpper, BabbleBlendshapeEnum.MouthRollUpper])
    MouthRollLower = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendshapeEnum.MouthRollLower, BabbleBlendshapeEnum.MouthRollLower])
    MouthRaiserUpper = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendshapeEnum.MouthShrugUpper, BabbleBlendshapeEnum.MouthRaiserUpper])
    MouthRaiserLower = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendshapeEnum.MouthShrugLower, BabbleBlendshapeEnum.MouthRaiserLower])
    MouthClosed = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendshapeEnum.MouthClose, BabbleBlendshapeEnum.MouthClosed])
    MouthSmileLeft = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendshapeEnum.MouthSmileLeft, BabbleBlendshapeEnum.MouthSmileLeft])
    MouthSmileRight = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendshapeEnum.MouthSmileRight, BabbleBlendshapeEnum.MouthSmileRight])
    MouthFrownLeft = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendshapeEnum.MouthFrownLeft, BabbleBlendshapeEnum.MouthFrownLeft])
    MouthFrownRight = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendshapeEnum.MouthFrownRight, BabbleBlendshapeEnum.MouthFrownRight])
    MouthDimpleLeft = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendshapeEnum.MouthDimpleLeft, BabbleBlendshapeEnum.MouthDimpleLeft])
    MouthDimpleRight = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendshapeEnum.MouthDimpleRight, BabbleBlendshapeEnum.MouthDimpleRight])
    MouthUpperUpLeft = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendshapeEnum.MouthUpperUpLeft, BabbleBlendshapeEnum.MouthUpperUpLeft])
    MouthUpperUpRight = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendshapeEnum.MouthUpperUpRight, BabbleBlendshapeEnum.MouthUpperUpRight])
    MouthLowerDownLeft = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendshapeEnum.MouthLowerDownLeft, BabbleBlendshapeEnum.MouthLowerDownLeft])
    MouthLowerDownRight = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendshapeEnum.MouthLowerDownRight, BabbleBlendshapeEnum.MouthLowerDownRight])
    MouthPressLeft = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendshapeEnum.MouthPressLeft, BabbleBlendshapeEnum.MouthPressLeft])
    MouthPressRight = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendshapeEnum.MouthPressRight, BabbleBlendshapeEnum.MouthPressRight])
    MouthStretchLeft = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendshapeEnum.MouthStretchLeft, BabbleBlendshapeEnum.MouthStretchLeft])
    MouthStretchRight = GeneralBlendShapeOption(
        same_as=[MediaPipeBlendshapeEnum.MouthStretchRight, BabbleBlendshapeEnum.MouthStretchRight])
    TongueOut = GeneralBlendShapeOption(
        same_as=[MediaPipeTongueBlendshapeEnum.TongueOut, BabbleBlendshapeEnum.TongueOut])
    TongueUp = GeneralBlendShapeOption(same_as=[BabbleBlendshapeEnum.TongueUp])
    TongueDown = GeneralBlendShapeOption(same_as=[BabbleBlendshapeEnum.TongueDown])
    TongueLeft = GeneralBlendShapeOption(same_as=[BabbleBlendshapeEnum.TongueLeft])
    TongueRight = GeneralBlendShapeOption(same_as=[BabbleBlendshapeEnum.TongueRight])
    TongueRoll = GeneralBlendShapeOption(same_as=[BabbleBlendshapeEnum.TongueRoll])
    TongueBendDown = GeneralBlendShapeOption(same_as=[BabbleBlendshapeEnum.TongueBendDown])
    TongueCurlUp = GeneralBlendShapeOption(same_as=[BabbleBlendshapeEnum.TongueCurlUp])
    TongueSquish = GeneralBlendShapeOption(same_as=[BabbleBlendshapeEnum.TongueSquish])
    TongueFlat = GeneralBlendShapeOption(same_as=[BabbleBlendshapeEnum.TongueFlat])
    TongueTwistLeft = GeneralBlendShapeOption(same_as=[BabbleBlendshapeEnum.TongueTwistLeft])
    TongueTwistRight = GeneralBlendShapeOption(same_as=[BabbleBlendshapeEnum.TongueTwistRight])

    # MediaPipe
    BrowDownLeft = GeneralBlendShapeOption(same_as=[MediaPipeBlendshapeEnum.BrowDownLeft])
    BrowDownRight = GeneralBlendShapeOption(same_as=[MediaPipeBlendshapeEnum.BrowDownRight])
    BrowInnerUp = GeneralBlendShapeOption(same_as=[MediaPipeBlendshapeEnum.BrowInnerUp])
    BrowOuterUpLeft = GeneralBlendShapeOption(same_as=[MediaPipeBlendshapeEnum.BrowOuterUpLeft])
    BrowOuterUpRight = GeneralBlendShapeOption(same_as=[MediaPipeBlendshapeEnum.BrowOuterUpRight])
    CheekPuff = GeneralBlendShapeOption(same_as=[MediaPipeBlendshapeEnum.CheekPuff])
    CheekSquintLeft = GeneralBlendShapeOption(same_as=[MediaPipeBlendshapeEnum.CheekSquintLeft])
    CheekSquintRight = GeneralBlendShapeOption(same_as=[MediaPipeBlendshapeEnum.CheekSquintRight])
    EyeBlinkLeft = GeneralBlendShapeOption(same_as=[MediaPipeBlendshapeEnum.EyeBlinkLeft])
    EyeBlinkRight = GeneralBlendShapeOption(same_as=[MediaPipeBlendshapeEnum.EyeBlinkRight])
    EyeLookDownLeft = GeneralBlendShapeOption(same_as=[MediaPipeBlendshapeEnum.EyeLookDownLeft])
    EyeLookDownRight = GeneralBlendShapeOption(same_as=[MediaPipeBlendshapeEnum.EyeLookDownRight])
    EyeLookInLeft = GeneralBlendShapeOption(same_as=[MediaPipeBlendshapeEnum.EyeLookInLeft])
    EyeLookInRight = GeneralBlendShapeOption(same_as=[MediaPipeBlendshapeEnum.EyeLookInRight])
    EyeLookOutLeft = GeneralBlendShapeOption(same_as=[MediaPipeBlendshapeEnum.EyeLookOutLeft])
    EyeLookOutRight = GeneralBlendShapeOption(same_as=[MediaPipeBlendshapeEnum.EyeLookOutRight])
    EyeLookUpLeft = GeneralBlendShapeOption(same_as=[MediaPipeBlendshapeEnum.EyeLookUpLeft])
    EyeLookUpRight = GeneralBlendShapeOption(same_as=[MediaPipeBlendshapeEnum.EyeLookUpRight])
    EyeSquintLeft = GeneralBlendShapeOption(same_as=[MediaPipeBlendshapeEnum.EyeSquintLeft])
    EyeSquintRight = GeneralBlendShapeOption(same_as=[MediaPipeBlendshapeEnum.EyeSquintRight])
    EyeWideLeft = GeneralBlendShapeOption(same_as=[MediaPipeBlendShapeEnum.EyeWideLeft])
    EyeWideRight = GeneralBlendShapeOption(same_as=[MediaPipeBlendshapeEnum.EyeWideRight])
    HeadX = GeneralBlendShapeOption(same_as=[MediaPipeBlendshapeEnum.HeadX], min_value=-1.0, has_center=True)
    HeadY = GeneralBlendShapeOption(same_as=[MediaPipeBlendshapeEnum.HeadY], min_value=-1.0, has_center=True)
    HeadZ = GeneralBlendShapeOption(same_as=[MediaPipeBlendshapeEnum.HeadZ], min_value=-1.0, has_center=True)
    HeadRotation = GeneralBlendShapeOption(same_as=[MediaPipeBlendShapeEnum.HeadRotation], disable_calibration=True)
