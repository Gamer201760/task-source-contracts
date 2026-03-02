from logging import getLogger

from usecase.interface import DataSource

logger = getLogger(__name__)


class ProcessJobs:
    def __init__(self, sources: list[DataSource] | None = None) -> None:
        self._sources = [] if sources is None else sources

    def add_source(self, src: DataSource) -> None:
        self._sources.append(src)

    def execute(self) -> None:
        for src in self._sources:
            logger.info(f'Jobs from {src.__class__.__name__}: {src.get_tasks()}')
