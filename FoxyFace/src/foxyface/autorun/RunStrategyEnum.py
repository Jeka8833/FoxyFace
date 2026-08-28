from enum import StrEnum, unique


@unique
class RunStrategyEnum(StrEnum):
    DISABLED = "disabled"
    USING_STEAM = "steam"
    USING_PATH = "path"
