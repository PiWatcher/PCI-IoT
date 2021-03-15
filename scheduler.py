from apscheduler.schedulers.blocking import BlockingScheduler
import os
import time
from detect import *
from load_model import *
from picamera import PiCamera

TIME_FRAME = 5
IMG_PATH = "./data/images/protoTest.jpg"
camera = PiCamera()

scheduler = BlockingScheduler()
print("Loading Model")
loaded_model,infer = load_model()

def job():
    camera.capture(IMG_PATH)
    detect(load_model, infer, 416, IMG_PATH)


def startScheduler(time_frame):

    scheduler.add_job(job, 'interval', seconds=time_frame)

    scheduler.start()

def stopScheduler():
    scheduler.stop()

def main():
    startScheduler(TIME_FRAME)

main()