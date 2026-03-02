from typing import Protocol, runtime_checkable

from domain.job import Job


@runtime_checkable
class DataSource(Protocol):
    def get_tasks(self) -> list[Job]: ...
