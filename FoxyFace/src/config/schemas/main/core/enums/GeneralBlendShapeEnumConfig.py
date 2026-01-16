from enum import StrEnum, unique

from src.stream.postprocessing.GeneralBlendShapeEnum import GeneralBlendShapeEnum


@unique
class GeneralBlendShapeEnumConfig(StrEnum):
    CheekPuffLeft = GeneralBlendShapeEnum.CheekPuffLeft.name
    CheekPuffRight = GeneralBlendShapeEnum.CheekPuffRight.name
    CheekSuckLeft = GeneralBlendShapeEnum.CheekSuckLeft.name
    CheekSuckRight = GeneralBlendShapeEnum.CheekSuckRight.name
    JawOpen = GeneralBlendShapeEnum.JawOpen.name
    JawForward = GeneralBlendShapeEnum.JawForward.name
    JawLeft = GeneralBlendShapeEnum.JawLeft.name
    JawRight = GeneralBlendShapeEnum.JawRight.name
    NoseSneerLeft = GeneralBlendShapeEnum.NoseSneerLeft.name
    NoseSneerRight = GeneralBlendShapeEnum.NoseSneerRight.name
    MouthFunnel = GeneralBlendShapeEnum.MouthFunnel.name
    MouthPucker = GeneralBlendShapeEnum.MouthPucker.name
    MouthLeft = GeneralBlendShapeEnum.MouthLeft.name
    MouthRight = GeneralBlendShapeEnum.MouthRight.name
    MouthRollUpper = GeneralBlendShapeEnum.MouthRollUpper.name
    MouthRollLower = GeneralBlendShapeEnum.MouthRollLower.name
    MouthRaiserUpper = GeneralBlendShapeEnum.MouthRaiserUpper.name
    MouthRaiserLower = GeneralBlendShapeEnum.MouthRaiserLower.name
    MouthClosed = GeneralBlendShapeEnum.MouthClosed.name
    MouthSmileLeft = GeneralBlendShapeEnum.MouthSmileLeft.name
    MouthSmileRight = GeneralBlendShapeEnum.MouthSmileRight.name
    MouthFrownLeft = GeneralBlendShapeEnum.MouthFrownLeft.name
    MouthFrownRight = GeneralBlendShapeEnum.MouthFrownRight.name
    MouthDimpleLeft = GeneralBlendShapeEnum.MouthDimpleLeft.name
    MouthDimpleRight = GeneralBlendShapeEnum.MouthDimpleRight.name
    MouthUpperUpLeft = GeneralBlendShapeEnum.MouthUpperUpLeft.name
    MouthUpperUpRight = GeneralBlendShapeEnum.MouthUpperUpRight.name
    MouthLowerDownLeft = GeneralBlendShapeEnum.MouthLowerDownLeft.name
    MouthLowerDownRight = GeneralBlendShapeEnum.MouthLowerDownRight.name
    MouthPressLeft = GeneralBlendShapeEnum.MouthPressLeft.name
    MouthPressRight = GeneralBlendShapeEnum.MouthPressRight.name
    MouthStretchLeft = GeneralBlendShapeEnum.MouthStretchLeft.name
    MouthStretchRight = GeneralBlendShapeEnum.MouthStretchRight.name
    TongueOut = GeneralBlendShapeEnum.TongueOut.name
    TongueUp = GeneralBlendShapeEnum.TongueUp.name
    TongueDown = GeneralBlendShapeEnum.TongueDown.name
    TongueLeft = GeneralBlendShapeEnum.TongueLeft.name
    TongueRight = GeneralBlendShapeEnum.TongueRight.name
    TongueRoll = GeneralBlendShapeEnum.TongueRoll.name
    TongueBendDown = GeneralBlendShapeEnum.TongueBendDown.name
    TongueCurlUp = GeneralBlendShapeEnum.TongueCurlUp.name
    TongueSquish = GeneralBlendShapeEnum.TongueSquish.name
    TongueFlat = GeneralBlendShapeEnum.TongueFlat.name
    TongueTwistLeft = GeneralBlendShapeEnum.TongueTwistLeft.name
    TongueTwistRight = GeneralBlendShapeEnum.TongueTwistRight.name
    BrowDownLeft = GeneralBlendShapeEnum.BrowDownLeft.name
    BrowDownRight = GeneralBlendShapeEnum.BrowDownRight.name
    BrowInnerUp = GeneralBlendShapeEnum.BrowInnerUp.name
    BrowOuterUpLeft = GeneralBlendShapeEnum.BrowOuterUpLeft.name
    BrowOuterUpRight = GeneralBlendShapeEnum.BrowOuterUpRight.name
    CheekPuff = GeneralBlendShapeEnum.CheekPuff.name
    CheekSquintLeft = GeneralBlendShapeEnum.CheekSquintLeft.name
    CheekSquintRight = GeneralBlendShapeEnum.CheekSquintRight.name
    EyeBlinkLeft = GeneralBlendShapeEnum.EyeBlinkLeft.name
    EyeBlinkRight = GeneralBlendShapeEnum.EyeBlinkRight.name
    EyeSquintLeft = GeneralBlendShapeEnum.EyeSquintLeft.name
    EyeSquintRight = GeneralBlendShapeEnum.EyeSquintRight.name
    EyeWideLeft = GeneralBlendShapeEnum.EyeWideLeft.name
    EyeWideRight = GeneralBlendShapeEnum.EyeWideRight.name
    EyeXLeft = GeneralBlendShapeEnum.EyeXLeft.name
    EyeXRight = GeneralBlendShapeEnum.EyeXRight.name
    EyeYLeft = GeneralBlendShapeEnum.EyeYLeft.name
    EyeYRight = GeneralBlendShapeEnum.EyeYRight.name
    HeadX = GeneralBlendShapeEnum.HeadX.name
    HeadY = GeneralBlendShapeEnum.HeadY.name
    HeadZ = GeneralBlendShapeEnum.HeadZ.name
    HeadPitch = GeneralBlendShapeEnum.HeadPitch.name
    HeadYaw = GeneralBlendShapeEnum.HeadYaw.name
    HeadRoll = GeneralBlendShapeEnum.HeadRoll.name

    def to_original(self) -> GeneralBlendShapeEnum:
        return GeneralBlendShapeEnum[self.name]

    @staticmethod
    def from_original(original: GeneralBlendShapeEnum) -> 'GeneralBlendShapeEnumConfig':
        return GeneralBlendShapeEnumConfig(original.name)
