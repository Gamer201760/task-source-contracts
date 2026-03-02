from random import Random

from domain.job import Job


class RandomJobsSource:
    def __init__(self, rnd: Random) -> None:
        self._rnd = rnd

    def get_tasks(self) -> list[Job]:
        return [
            Job(
                id=self._rnd.randint(10, 100000),
                payload={
                    'temperature': self._rnd.randint(-50, 100),
                    'humidity': self._rnd.randint(0, 100),
                },
            )
            for _ in range(self._rnd.randint(10, 30))
        ]
