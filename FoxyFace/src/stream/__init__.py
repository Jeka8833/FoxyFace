import logging

import onnxruntime

_logger = logging.getLogger(__name__)

onnxruntime.disable_telemetry_events()

try:
    import torch
except Exception:
    _logger.warning("Failed to import torch. Some compute acceleration for onnxruntime may not work")
