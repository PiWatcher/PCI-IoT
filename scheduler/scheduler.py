from apscheduler.schedulers.blocking import BlockingScheduler
import os
import time

scheduler = BlockingScheduler()

def job():
    cmd = "cd .. && cd yolov4-custom-functions && python detect.py"
    os.system(cmd)


def startScheduler(time_frame):

    scheduler.add_job(job, 'interval', seconds=time_frame)

    scheduler.start()

def stopScheduler():
    scheduler.stop()

def main():
    startScheduler(10)

main()