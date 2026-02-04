import logging
from pathlib import Path

_logger = logging.getLogger(__name__)


class PathUtil:
    @staticmethod
    def to_path_or_default(path: str | Path | None, default: str | Path, strict: bool = True) -> Path:
        try:
            if path and not path.isspace():
                return Path(path).resolve(strict=strict)
        except Exception:
            _logger.warning(f"Failed to resolve path: {path}", exc_info=True, stack_info=True)

        return Path(default).resolve(strict=strict)

    @staticmethod
    def to_path(path: str | None, strict: bool = True) -> Path | None:
        try:
            if path and not path.isspace():
                return Path(path).resolve(strict=strict)
        except Exception:
            _logger.warning(f"Failed to resolve path: {path}", exc_info=True, stack_info=True)

        return None
