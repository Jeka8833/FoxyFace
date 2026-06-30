from dataclasses import dataclass

from blendshape_router.facades.babble import BabbleDefaultValue

from src.config.schemas.main.core.enums.BabbleProtocolEnumConfig import BabbleProtocolEnumConfig


@dataclass(slots=True)
class BabbleSenderConfig:
    enabled: bool = True

    ip: str = BabbleDefaultValue.OSC_IP
    port: int = BabbleDefaultValue.OSC_PORT

    protocol_version: BabbleProtocolEnumConfig = BabbleProtocolEnumConfig.MaximumCompatibility

    solver_enabled: bool = True
    solver_model_path: str = ""
    solver_threads: int = BabbleDefaultValue.SOLVER_THREADS
    solver_max_cps: float = BabbleDefaultValue.SOLVER_MAX_CPS
    solver_interleaved_vertices_percentage: float = 0.8

    osc_cache_invalidate_timeout: float = BabbleDefaultValue.OSC_CACHE_INVALIDATE_TIMEOUT
    osc_cache_full_sync_period: float = BabbleDefaultValue.OSC_CACHE_FULL_SYNC_PERIOD
    osc_cache_float_precision: float = BabbleDefaultValue.OSC_CACHE_FLOAT_PRECISION
    osc_bundle_size: int = BabbleDefaultValue.OSC_BUNDLE_SIZE

    test_send_period: float = BabbleDefaultValue.ENCODER_TEST_SEND_PERIOD
    test_animation_period: float = BabbleDefaultValue.ENCODER_TEST_ANIMATION_PERIOD
