from dataclasses import dataclass, field

from config.schemas.core.sender.FoxyFaceSenderConfig import FoxyFaceSenderConfig
from config.schemas.core.sender.IFacialMocapSenderConfig import IFacialMocapSenderConfig
from config.schemas.core.sender.MeowFaceSenderConfig import MeowFaceSenderConfig
from config.schemas.core.sender.VRChatSenderConfig import VRChatSenderConfig


@dataclass(slots=True)
class SenderConfig:
    foxyface: FoxyFaceSenderConfig = field(default_factory=FoxyFaceSenderConfig)
    ifacialmocap: IFacialMocapSenderConfig = field(default_factory=IFacialMocapSenderConfig)
    meowface: MeowFaceSenderConfig = field(default_factory=MeowFaceSenderConfig)
    vrchat: VRChatSenderConfig = field(default_factory=VRChatSenderConfig)
