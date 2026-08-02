from enum import StrEnum

from blendshape_router.facades.babble.BabbleGraphVersion import BabbleGraphVersion


class BabbleProtocolEnumConfig(StrEnum):
    MaximumCompatibility = "Maximum Compatibility"
    V2 = "v2"

    @property
    def original_value(self) -> BabbleGraphVersion:
        match self:
            case BabbleProtocolEnumConfig.MaximumCompatibility:
                return BabbleGraphVersion.MAXIMUM_COMPATIBILITY
            case BabbleProtocolEnumConfig.V2:
                return BabbleGraphVersion.V2
            case _:
                raise ValueError("Unknown protocol")

    @staticmethod
    def from_original(original: BabbleGraphVersion) -> 'BabbleProtocolEnumConfig':
        match original:
            case BabbleGraphVersion.MAXIMUM_COMPATIBILITY:
                return BabbleProtocolEnumConfig.MaximumCompatibility
            case BabbleGraphVersion.V2:
                return BabbleProtocolEnumConfig.V2
            case _:
                raise ValueError("Unknown protocol")
