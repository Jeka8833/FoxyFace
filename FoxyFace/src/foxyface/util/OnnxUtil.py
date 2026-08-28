import logging
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
    if name is not None and not isinstance(name, str):
        raise TypeError(f"Provider 'name' must be a string, got {type(name).__name__}")

    if not isinstance(gpu_id, int) or gpu_id < 0:
        raise ValueError(f"'gpu_id' must be a non-negative integer, got {gpu_id}")

    out: list[str | tuple[str, dict[Any, Any]]] = []

    if is_auto(name):
        for provider, value in _PROVIDERS.items():
            if _DEVICE_ID_KEY in value:
                out.append((provider, {_DEVICE_ID_KEY: str(gpu_id)}))
            else:
                out.append(provider)
    else:
        provider_params = _PROVIDERS.get(name)

        if _DEVICE_ID_KEY in provider_params:
            out.append((name, {_DEVICE_ID_KEY: str(gpu_id)}))
        else:
            out.append(name)

    return out


def is_auto(name: str | None) -> bool:
    return name is None or name not in _PROVIDERS
