from absl import app, flags, logging
WEIGHTS = "./checkpoints/yolov4-416"
import time
from tensorflow.python.saved_model import tag_constants
import tensorflow as tf

def load_model():
    try:
        start_before = time.perf_counter()
        saved_model_loaded = tf.saved_model.load(WEIGHTS, tags=[tag_constants.SERVING])
        infer = saved_model_loaded.signatures['serving_default']
        end = time.perf_counter()
        print(end - start_before)
        return saved_model_loaded,infer
    
    except:
        raise Exception("Model Incorrectly loaded")
        return - 9999

