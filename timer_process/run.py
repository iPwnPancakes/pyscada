from dotenv import load_dotenv

from Process import Process
from jobs.hello import HelloWorld

load_dotenv()

process = Process()

process.register_job(HelloWorld('* * * * * *'))

process.run()
