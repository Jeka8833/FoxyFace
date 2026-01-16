from typing import Protocol, TypeVar

from dataclass_wizard import JSONWizard

T = TypeVar("T", bound=JSONWizard)


class MigrationManager(Protocol[T]):
    def try_migrate(self, config: T) -> None: ...
