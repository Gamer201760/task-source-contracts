from domain.job import Job


class MockExternalSource:
    def get_tasks(self) -> list[Job]:
        return [Job(id=1, payload={'palka': 'copalka'})]
