from dataclasses import dataclass

from src.autorun.RunStrategyEnum import RunStrategyEnum


@dataclass(slots=True)
class AutoRunOptions:
    vrchat_strategy: RunStrategyEnum = RunStrategyEnum.DISABLED
    vrchat_path: str = ""

    vrcft_strategy: RunStrategyEnum = RunStrategyEnum.DISABLED
    vrcft_path: str = ""
