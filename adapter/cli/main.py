from logging import INFO, basicConfig, getLogger
from random import Random

from repository.api.mock import MockExternalSource
from repository.generator.rand import RandomJobsSource
from usecase.process import ProcessTasks

basicConfig(format='[%(levelname)s] %(name)s %(asctime)s %(message)s', level=INFO)
logger = getLogger(__name__)


def main():
    logger.info('Waiting data...')
    process = ProcessTasks(
        [
            MockExternalSource(),
        ]
    )
    process.add_source(
        RandomJobsSource(Random(1)),
    )
    process.execute()


if __name__ == '__main__':
    main()
