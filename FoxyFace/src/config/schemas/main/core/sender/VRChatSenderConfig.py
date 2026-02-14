from dataclasses import dataclass, field

from blendshape_router.facades.vrchat import VRChatDefaultValue


@dataclass(slots=True)
class VRChatSenderConfig:
    enabled: bool = True

    blocked_ips: list[str] = field(default_factory=list)

    avatar_update_period: float = VRChatDefaultValue.AVATAR_UPDATE_PERIOD
    avatar_error_sleep_time: float = VRChatDefaultValue.AVATAR_ERROR_SLEEP_TIME
    avatar_close_connection_after_retries: int = VRChatDefaultValue.AVATAR_CLOSE_CONNECTION_AFTER_RETRIES
    zeroconf_timeout: float = VRChatDefaultValue.ZEROCONF_TIMEOUT

    solver_enabled: bool = True
    solver_model_path: str = ""
    solver_threads: int = VRChatDefaultValue.SOLVER_THREADS
    solver_max_cps: float = VRChatDefaultValue.SOLVER_MAX_CPS
    solver_interleaved_vertices_percentage: float = 0.8

    cache_invalidate_timeout: float = VRChatDefaultValue.OSC_CACHE_INVALIDATE_TIMEOUT
    cache_full_sync_period: float = VRChatDefaultValue.OSC_CACHE_FULL_SYNC_PERIOD
    cache_float_precision: float = VRChatDefaultValue.OSC_CACHE_FLOAT_PRECISION
    osc_bundle_size: int = VRChatDefaultValue.OSC_BUNDLE_SIZE

    allow_legacy_graph: bool = VRChatDefaultValue.ALLOW_LEGACY_GRAPH
    parser_max_binary_bits: int = VRChatDefaultValue.PARSER_MAX_BINARY_BITS
    test_send_period: float = VRChatDefaultValue.ENCODER_TEST_SEND_PERIOD
    test_animation_period: float = VRChatDefaultValue.ENCODER_TEST_ANIMATION_PERIOD
