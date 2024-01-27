from datetime import datetime

from utils.Job import Job


class Cron:
    def __init__(self):
        self.jobs = []

    def schedule(self, current_time: datetime):
        for job in self.jobs:
            if job.should_run(current_time):
                job.run()

    def add_job(self, job: Job):
        self.jobs.append(job)
