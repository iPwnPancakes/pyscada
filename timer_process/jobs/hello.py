from utils.Job import Job


class HelloWorld(Job):
    def __init__(self, schedule: str):
        super().__init__(schedule=schedule)

    def run(self):
        print('Hello, world!')
