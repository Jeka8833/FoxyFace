import logging
from importlib import resources
from importlib.resources.abc import Traversable

from foxyface.AppConstants import AppConstants

__logger = logging.getLogger(__name__)


def play_start_sound():
    __run_play_for_file(AppConstants.get_file_from_assets("start.opus"))


def play_good_sound():
    __run_play_for_file(AppConstants.get_file_from_assets("good.opus"))


def play_fail_sound():
    __run_play_for_file(AppConstants.get_file_from_assets("fail.opus"))


def __run_play_for_file(file_ref: Traversable):
    try:
        # WSL or other platforms that doesn't support sounddevice
        import sounddevice
        import soundfile

        with resources.as_file(file_ref) as path:
            data, fs = soundfile.read(path)
            sounddevice.play(data, fs)
    except Exception:
        __logger.warning("Failed to play sound", exc_info=True, stack_info=True)
