from enum import StrEnum

from blendshape_router.facades.vrchat.VRChatGraphVersion import VRChatGraphVersion


class VRChatProtocolEnumConfig(StrEnum):
    MaximumCompatibility = "Maximum Compatibility"
    V4 = "v4"

    @property
    def original_value(self) -> VRChatGraphVersion:
        match self:
            case VRChatProtocolEnumConfig.MaximumCompatibility:
                return VRChatGraphVersion.MAXIMUM_COMPATIBILITY
            case VRChatProtocolEnumConfig.V4:
                return VRChatGraphVersion.V4
            case _:
                raise ValueError("Unknown protocol")

    @staticmethod
    def from_original(original: VRChatGraphVersion) -> 'VRChatProtocolEnumConfig':
        match original:
            case VRChatGraphVersion.MAXIMUM_COMPATIBILITY:
                return VRChatProtocolEnumConfig.MaximumCompatibility
            case VRChatGraphVersion.V4:
                return VRChatProtocolEnumConfig.V4
            case _:
                raise ValueError("Unknown protocol")
