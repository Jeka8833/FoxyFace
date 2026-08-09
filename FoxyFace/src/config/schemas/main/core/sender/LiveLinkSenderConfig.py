from dataclasses import dataclass

from blendshape_router.facades.livelink import LiveLinkDefaultValue


@dataclass(slots=True)
class LiveLinkSenderConfig:
    enabled: bool = False

    subject_name: str | None = LiveLinkDefaultValue.SUBJECT_NAME
    device_id: str | None = None
    fps_numerator: int = LiveLinkDefaultValue.FPS.numerator
    fps_denominator: int = LiveLinkDefaultValue.FPS.denominator

    ip: str = "127.0.0.1"
    port: int = 11111

    solver_enabled: bool = True
    solver_model_path: str = ""
    solver_threads: int = LiveLinkDefaultValue.SOLVER_THREADS
    solver_max_cps: float = LiveLinkDefaultValue.SOLVER_MAX_CPS
    solver_interleaved_vertices_percentage: float = 0.8

    cache_invalidate_timeout: float = LiveLinkDefaultValue.UDP_CACHE_INVALIDATE_TIMEOUT
    cache_full_sync_period: float = LiveLinkDefaultValue.UDP_CACHE_FULL_SYNC_PERIOD
    cache_float_precision: float = LiveLinkDefaultValue.UDP_CACHE_FLOAT_PRECISION
    udp_ping_interval: float = LiveLinkDefaultValue.UDP_PING_INTERVAL
    crash_sleep_time: float = LiveLinkDefaultValue.CRASH_SLEEP_TIME

    test_send_period: float = LiveLinkDefaultValue.ENCODER_TEST_SEND_PERIOD
    test_animation_period: float = LiveLinkDefaultValue.ENCODER_TEST_ANIMATION_PERIOD
