from dataclasses import dataclass

from blendshape_router.facades.foxyface import FoxyFaceDefaultValue


@dataclass(slots=True)
class FoxyFaceSenderConfig:
    enabled: bool = True

    auto_connect_enabled: bool = FoxyFaceDefaultValue.UDP_AUTO_CONNECT_ENABLED
    ip: str = "localhost"
    port: int = 12345

    test_send_period: float = FoxyFaceDefaultValue.ENCODER_TEST_SEND_PERIOD
    test_animation_period: float = FoxyFaceDefaultValue.ENCODER_TEST_ANIMATION_PERIOD

    solver_enabled: bool = True
    solver_model_path: str = ""
    solver_threads: int = FoxyFaceDefaultValue.SOLVER_THREADS
    solver_max_cps: float = FoxyFaceDefaultValue.SOLVER_MAX_CPS
    solver_interleaved_vertices_percentage: float = 0.8

    cache_invalidate_timeout: float = FoxyFaceDefaultValue.UDP_CACHE_INVALIDATE_TIMEOUT
    cache_full_sync_period: float = FoxyFaceDefaultValue.UDP_CACHE_FULL_SYNC_PERIOD
    cache_float_precision: float = FoxyFaceDefaultValue.UDP_CACHE_FLOAT_PRECISION
    udp_ping_interval: float = FoxyFaceDefaultValue.UDP_PING_INTERVAL

    auto_connect_port: int = FoxyFaceDefaultValue.AUTO_CONNECT_PORT