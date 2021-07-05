import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import cv2

model = tf.keras.models.load_model("")
model._make_predict_function()

def get_pred(image):
    im_arr = np.array(image)
    im_arr = cv2.resize(im_arr, (150, 150))
    im_arr = np.array([im_arr])
    tf.reset_default_graph()
    raw_pred = model.predict(im_arr)[0]
    pred = np.argmax(raw_pred)
    return pred


def get_class(image):
    pred = get_pred(image)
    return "organic or non-recyclable" if pred == 0 else "recyclable"

