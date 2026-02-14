from dataclasses import dataclass

from blendshape_router.facades.ifacialmocap import IFacialMocapDefaultValue


@dataclass(slots=True)
class IFacialMocapSenderConfig:
    enabled: bool = False

    facemotion3d_compatibility: bool = IFacialMocapDefaultValue.FACEMOTION3D_COMPATIBILITY

    auto_connect_enabled: bool = IFacialMocapDefaultValue.AUTO_CONNECT_ENABLED
    ip: str = "127.0.0.1"
    port: int = 49983

    solver_enabled: bool = True
    solver_model_path: str = ""
    solver_threads: int = IFacialMocapDefaultValue.SOLVER_THREADS
    solver_max_cps: float = IFacialMocapDefaultValue.SOLVER_MAX_CPS
    solver_interleaved_vertices_percentage: float = 0.8

    cache_invalidate_timeout: float = IFacialMocapDefaultValue.UDP_CACHE_INVALIDATE_TIMEOUT
    cache_full_sync_period: float = IFacialMocapDefaultValue.UDP_CACHE_FULL_SYNC_PERIOD
    cache_float_precision: float = IFacialMocapDefaultValue.UDP_CACHE_FLOAT_PRECISION
    udp_ping_interval: float = IFacialMocapDefaultValue.UDP_PING_INTERVAL

    auto_connect_port: int = IFacialMocapDefaultValue.AUTO_CONNECT_PORT
    test_send_period: float = IFacialMocapDefaultValue.ENCODER_TEST_SEND_PERIOD
    test_animation_period: float = IFacialMocapDefaultValue.ENCODER_TEST_ANIMATION_PERIOD
