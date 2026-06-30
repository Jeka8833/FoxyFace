from enum import StrEnum

from blendshape_router.plugin.endpoints.babble.ProtocolVersion import ProtocolVersion


class BabbleProtocolEnumConfig(StrEnum):
    MaximumCompatibility = "Maximum Compatibility"
    V2 = "v2"

    @property
    def original_value(self) -> ProtocolVersion:
        match self:
            case BabbleProtocolEnumConfig.MaximumCompatibility:
                return ProtocolVersion.MAXIMUM_COMPATIBILITY
            case BabbleProtocolEnumConfig.V2:
                return ProtocolVersion.V2
            case _:
                raise ValueError("Unknown protocol")

    @staticmethod
    def from_original(original: ProtocolVersion) -> 'BabbleProtocolEnumConfig':
        match original:
            case ProtocolVersion.MAXIMUM_COMPATIBILITY:
                return BabbleProtocolEnumConfig.MaximumCompatibility
            case ProtocolVersion.V2:
                return BabbleProtocolEnumConfig.V2
            case _:
                raise ValueError("Unknown protocol")
