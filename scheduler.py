from apscheduler.schedulers.blocking import BlockingScheduler
import os
import time
from detect import *
from load_model import *
from picamera import PiCamera

TIME_FRAME = 5
IMG_PATH = "./data/images/protoTest.jpg"
camera = PiCamera()

BldgName = os.getenv("BLDGNAME")
BldgNum = os.getenv("BLDGNUM")
EndPtName = os.getenv("ENDPOINTNAME")
EndPtId = os.getenv("ENDPOINTID")
ip_addr = os.getenv("IPADDRESS")

endpoint_info = [BldgNum, BldgName, EndPtId, EndPtName, 0]

scheduler = BlockingScheduler()
print("Loading Model")
loaded_model,infer = load_model()

def job():
    camera.capture(IMG_PATH)
    detect(load_model, infer, 416, IMG_PATH, endpoint_info, ip_addr)


def startScheduler(time_frame):

    scheduler.add_job(job, 'interval', seconds=time_frame)

    scheduler.start()

def stopScheduler():
    scheduler.stop()

def main():
    startScheduler(TIME_FRAME)

main()