import time
from datetime import datetime

from utils.Cron import Cron
from utils.Job import Job


class Process:
    def __init__(self):
        self.scheduler = Cron()

    def register_job(self, job: Job):
        self.scheduler.add_job(job)

    def run(self):
        while True:
            time.sleep(1)
            self.scheduler.schedule(datetime.now())
