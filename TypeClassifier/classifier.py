import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import cv2

def get_pred(image, model):
    # im_arr = np.array(image)
    im_arr = cv2.resize(image, (150,150))
    im_arr = np.array([im_arr])
    raw_pred = model.predict(im_arr)[0]
    pred = np.argmax(raw_pred)
    return pred

def get_class(pred):
    return "organic or non-recyclable" if pred == 0 else "recyclable"
