from dataclasses import dataclass

from blendshape_router.facades.meowface import MeowFaceDefaultValue


@dataclass(slots=True)
class MeowFaceSenderConfig:
    enabled: bool = False

    auto_connect_enabled: bool = MeowFaceDefaultValue.AUTO_CONNECT_ENABLED
    ip: str = "127.0.0.1"
    port: int = 12345

    solver_enabled: bool = True
    solver_model_path: str = ""
    solver_threads: int = MeowFaceDefaultValue.SOLVER_THREADS
    solver_max_cps: float = MeowFaceDefaultValue.SOLVER_MAX_CPS
    solver_interleaved_vertices_percentage: float = 0.8

    cache_invalidate_timeout: float = MeowFaceDefaultValue.UDP_CACHE_INVALIDATE_TIMEOUT
    cache_full_sync_period: float = MeowFaceDefaultValue.UDP_CACHE_FULL_SYNC_PERIOD
    cache_float_precision: float = MeowFaceDefaultValue.UDP_CACHE_FLOAT_PRECISION
    udp_ping_interval: float = MeowFaceDefaultValue.UDP_PING_INTERVAL

    avatar_config_file: str = ""

    auto_connect_port: int = MeowFaceDefaultValue.AUTO_CONNECT_PORT
    test_send_period: float = MeowFaceDefaultValue.ENCODER_TEST_SEND_PERIOD
    test_animation_period: float = MeowFaceDefaultValue.ENCODER_TEST_ANIMATION_PERIOD
