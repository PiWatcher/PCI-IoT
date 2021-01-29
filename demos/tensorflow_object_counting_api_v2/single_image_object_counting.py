#----------------------------------------------
#--- Author         : Ahmet Ozlu
#--- Mail           : ahmetozlu93@gmail.com
#--- Date           : 27th January 2018
#----------------------------------------------

# Imports
import tensorflow as tf
import cv2
import os
import time
import picamera

# Object detection imports
from utils import backbone
from api import object_counting_api

defaultCamera = 0

start = time.perf_counter()

with picamera.PiCamera() as camera:
    camera.resolution = (640, 640)
    time.sleep(2)
    camera.capture("./images/test.jpg")

#video = cv2.VideoCapture(defaultCamera)

#ret, frame = video.read()

if not os.path.exists("images"):
    os.makedirs("images")


input_image = "./images/test1.jpg"

#input_video = "./input_images_and_videos/lecture-hall_front_2.jpg"


# By default I use an "SSD with Mobilenet" model here. See the detection model zoo (https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md) for a list of other models that can be run out-of-the-box with varying speeds and accuracies.
detection_graph, category_index = backbone.set_model('ssd_mobilenet_v2_coco_2018_03_29', 'mscoco_label_map.pbtxt')

is_color_recognition_enabled = 0

result = object_counting_api.single_image_object_counting(input_image, detection_graph, category_index, is_color_recognition_enabled) # targeted objects counting

end = time.perf_counter()

print (f"{end - start:0.4f}")
