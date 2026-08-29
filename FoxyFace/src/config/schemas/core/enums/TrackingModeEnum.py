from enum import StrEnum, unique


@unique
class TrackingModeEnum(StrEnum):
    MOUTH = "mouth"
    EYES = "eyes"
    BOTH = "both"