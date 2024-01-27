from datetime import datetime

from utils.Job import Job


class HelloWorld(Job):
    def __init__(self, schedule: str):
        super().__init__(schedule=schedule)

    def run(self):
        print(f'Hello, world! @ {self.last_run}')
        self.last_run = datetime.now()

