import logging
from pathlib import Path

from AppConstants import AppConstants

__logger = logging.getLogger(__name__)


def play_start_sound():
    __run_play_for_file(AppConstants.get_application_root() / 'Assets' / 'start.opus')


def play_good_sound():
    __run_play_for_file(AppConstants.get_application_root() / 'Assets' / 'good.opus')


def play_fail_sound():
    __run_play_for_file(AppConstants.get_application_root() / 'Assets' / 'fail.opus')


def __run_play_for_file(file: Path):
    try:
        # WSL or other platforms that doesn't support sounddevice
        import sounddevice
        import soundfile

        data, fs = soundfile.read(file)
        sounddevice.play(data, fs)
    except Exception:
        __logger.warning("Failed to play sound", exc_info=True, stack_info=True)
