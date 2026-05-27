import logging
from contextlib import nullcontext
from threading import Lock
from types import MappingProxyType
from typing import Sequence, Any

_logger = logging.getLogger(__name__)

try:
    import torch
except ImportError:
    _logger.info("Failed to import torch. Some compute acceleration for onnxruntime may not work")

import onnxruntime

onnxruntime.disable_telemetry_events()

_DEVICE_ID_KEY = "device_id"

_AVAILABLE_ONNX_PROVIDERS = onnxruntime.get_available_providers()
_logger.info(f"All supported providers for onnxruntime: {_AVAILABLE_ONNX_PROVIDERS}")

global_lock = Lock() if "DmlExecutionProvider" in _AVAILABLE_ONNX_PROVIDERS else nullcontext()

_ALLOWED_PROVIDERS = {
    "DmlExecutionProvider": [_DEVICE_ID_KEY],
    "CUDAExecutionProvider": [_DEVICE_ID_KEY],
    "ROCMExecutionProvider": [_DEVICE_ID_KEY],
    "CoreMLExecutionProvider": [],
    "CPUExecutionProvider": []
}

_PROVIDERS = {
    name: params
    for name, params in _ALLOWED_PROVIDERS.items()
    if name in _AVAILABLE_ONNX_PROVIDERS
}
_logger.info(f"Available providers: {_PROVIDERS}")

AVAILABLE_PROVIDERS: MappingProxyType[str, bool] = MappingProxyType({
    provider: _DEVICE_ID_KEY in params
    for provider, params in _PROVIDERS.items()
})


def get_provider(name: str | None, gpu_id: int = 0) -> Sequence[str | tuple[str, dict[Any, Any]]]:
    name = get_provider_name_or_first(name)

    provider_params = _PROVIDERS.get(name)
    if provider_params is None:
        available_names = ", ".join(repr(k) for k in _PROVIDERS.keys())

        raise ValueError(
            f"Provider '{name}' is not supported or not available on this system. "
            f"Available providers are: {available_names}"
        )

    if _DEVICE_ID_KEY in provider_params:
        if not isinstance(gpu_id, int) or gpu_id < 0:
            raise ValueError(f"'gpu_id' must be a non-negative integer, got {gpu_id}")

        return [(name, {_DEVICE_ID_KEY: str(gpu_id)})]

    return [name]


def get_provider_name_or_first(name: str | None) -> str:
    if name is not None and not isinstance(name, str):
        raise TypeError(f"Provider 'name' must be a string, got {type(name).__name__}")

    if name is None or name not in _PROVIDERS:
        return next(iter(_PROVIDERS))

    return name
