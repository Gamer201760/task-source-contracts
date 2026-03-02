from logging import INFO, basicConfig, getLogger
from random import Random

from repository.api.mock import MockExternalSource
from repository.generator.rand import RandomJobsSource
from usecase.process import ProcessJobs

basicConfig(format='[%(levelname)s] %(name)s %(asctime)s %(message)s', level=INFO)
logger = getLogger(__name__)


def main():
    logger.info('Hello')
    process_jobs = ProcessJobs(
        [
            MockExternalSource(),
            RandomJobsSource(Random()),
        ]
    )
    process_jobs.execute()


if __name__ == '__main__':
    main()
