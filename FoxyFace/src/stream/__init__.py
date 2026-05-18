import logging
import os

import onnxruntime

_logger = logging.getLogger(__name__)

onnxruntime.disable_telemetry_events()

try:
    import torch
except Exception:
    _logger.warning("Failed to import torch. Some compute acceleration for onnxruntime may not work")

# https://github.com/google-ai-edge/mediapipe/issues/6291
# I don't know how to disable mediapipe telemetry

os.environ["GLOG_minloglevel"] = "3"
os.environ["GOOGLE_GLOG_minloglevel"] = "3"
os.environ["GOOGLE_LOG_TO_STDERR"] = "1"
os.environ["GLOG_logtostderr"] = "1"
os.environ["MEDIAPIPE_TELEMETRY_URL"] = ""
