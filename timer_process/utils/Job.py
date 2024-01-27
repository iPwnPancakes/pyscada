from datetime import datetime

from croniter import croniter


class Job:
    def __init__(self, schedule: str | None = None, command: callable = None):
        self.schedule: str | None = schedule
        self.command: callable = command
        self.last_run: datetime | None = None

    def should_run(self, current_time: datetime) -> bool:
        if self.schedule is None:
            return False

        if self.last_run is None:
            return True

        schedule_itr = croniter(self.schedule, self.last_run)
        if current_time >= schedule_itr.get_next(datetime):
            return True

    def run(self):
        raise NotImplementedError
