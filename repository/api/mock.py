import time

from domain.job import Job


class MockExternalSource:
    def get_tasks(self) -> list[Job]:
        time.sleep(1)  # задержка, имитация хождения по сети
        return [Job(id=1, payload={'palka': 'copalka'})]
