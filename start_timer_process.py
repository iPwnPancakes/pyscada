from dotenv import load_dotenv

from timer_process.Process import Process
from timer_process.jobs.PollTagModbusValues import PollTagModbusValues
from timer_process.jobs.hello import HelloWorld

load_dotenv()

process = Process()

process.register_job(HelloWorld('* * * * * *'))
process.register_job(PollTagModbusValues('* * * * * *'))

process.run()
