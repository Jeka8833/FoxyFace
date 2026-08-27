from dataclasses import dataclass
from difflib import SequenceMatcher
from typing import Self

from cv2_enumerate_cameras.camera_info import CameraInfo


@dataclass(slots=True, frozen=True)
class CameraEntry:
    index: int | str = 0
    name: str = ""
    path: str | None = None
    vid: int | None = None
    pid: int | None = None
    backend: int = 700
    manual: bool = False

    def compare(self, other: Self) -> float:
        score = SequenceMatcher(None, self.name, other.name).ratio() * 40

        if self.vid is not None and self.pid is not None and self.vid == other.vid and self.pid == other.pid:
            score += 45

        if self.path is not None and self.path == other.path:
            score += 10

        if self.index == other.index:
            score += 5

        if self.backend == other.backend:
            score += 100

        return score

    def change_manual(self, manual: bool) -> "CameraEntry":
        return CameraEntry(
            index=self.index,
            name=self.name,
            path=self.path,
            vid=self.vid,
            pid=self.pid,
            backend=self.backend,
            manual=manual
        )

    @staticmethod
    def create_using_camera_info(camera_info: CameraInfo) -> "CameraEntry":
        open_cv_index = camera_info.index + camera_info.backend

        index = open_cv_index % 100
        backend = (open_cv_index // 100) * 100

        return CameraEntry(
            index=index,
            name=camera_info.name,
            path=camera_info.path,
            vid=camera_info.vid,
            pid=camera_info.pid,
            backend=backend,
            manual=False
        )

    @staticmethod
    def create_using_backend_and_index(backend: int, index: int | str) -> "CameraEntry":
        return CameraEntry(
            index=index,
            name=f"Unknown camera {index}",
            path=index if isinstance(index, str) else None,
            vid=None,
            pid=None,
            backend=backend,
            manual=True
        )