import logging

import sounddevice
import soundfile

from AppConstants import AppConstants

__logger = logging.getLogger(__name__)


def play_start_sound():
    try:
        data, fs = soundfile.read(AppConstants.get_application_root() / 'Assets' / 'start.opus')
        sounddevice.play(data, fs)
    except Exception:
        __logger.warning("Failed to play sound", exc_info=True, stack_info=True)


def play_good_sound():
    try:
        data, fs = soundfile.read(AppConstants.get_application_root() / 'Assets' / 'good.opus')
        sounddevice.play(data, fs)
    except Exception:
        __logger.warning("Failed to play sound", exc_info=True, stack_info=True)


def play_fail_sound():
    try:
        data, fs = soundfile.read(AppConstants.get_application_root() / 'Assets' / 'fail.opus')
        sounddevice.play(data, fs)
    except Exception:
        __logger.warning("Failed to play sound", exc_info=True, stack_info=True)
