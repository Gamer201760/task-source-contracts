from logging import INFO, basicConfig, getLogger

from repository.api.mock import MockExternalSource
from usecase.process import ProcessJobs

basicConfig(format='[%(levelname)s] %(name)s %(asctime)s %(message)s', level=INFO)
logger = getLogger(__name__)


def main():
    logger.info('Hello')
    process_jobs = ProcessJobs(
        [
            MockExternalSource(),
        ]
    )
    process_jobs.execute()


if __name__ == '__main__':
    main()
