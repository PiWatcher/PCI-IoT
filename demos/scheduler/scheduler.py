import schedule
import os

def job():
    os.system("python test.py")

schedule.every(1).minutes.do(job)


while True:
    schedule.run_pending()