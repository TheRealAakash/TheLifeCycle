import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import cv2

model = tf.keras.models.load_model("D:\\Users\\Aakash\\Documents\\Programming\\Python\\Projects\\TheTrashCycle\\AakashCode\\TrashInference\\type-classifier3.model")


def get_pred(image):
    im_arr = np.array(image)
    im_arr = cv2.resize(im_arr, (150, 150))
    im_arr = np.array([im_arr])
    raw_pred = model.predict(im_arr)[0]
    pred = np.argmax(raw_pred)
    return pred


def get_class(pred):
    return "organic or non-recyclable" if pred == 0 else "recyclable"
