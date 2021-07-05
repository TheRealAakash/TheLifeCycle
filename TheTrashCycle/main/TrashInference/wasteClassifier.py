import cv2
import keras
from keras.applications.inception_v3 import InceptionV3
from keras.applications.inception_v3 import preprocess_input
from keras.applications.inception_v3 import decode_predictions

model = InceptionV3(weights='imagenet', include_top=True)
import numpy as np
import matplotlib.pyplot as plt
import skimage.transform

model._make_predict_function()


def predict(image):
    img = skimage.transform.resize(image, (299, 299)) * 255
    # x = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(np.array(img))
    #  plt.imshow(img[0])
    #     plt.show()
    features = model.predict(img)
    preds = decode_predictions(features, top=1000)
    label = ""
    keys = [
        "plastic",
        "wood",
        "glass",
        "bottle",
        "food",
        "apple",
        "banana",
        "mango",
        "melon",
        "ice",
        "cloth",
        "trash",
        "garbage",
        "waste",
        "oil",
    ]
    blacklist = ["bear",
                 "rabbit", "truck"]
    for l in preds[0]:
        l = str(l[1])
        for key in keys:
            if key in l:
                good = True
                for k in blacklist:
                    if k in l:
                        good = False
                        break
                if good:
                    label = l
                    break
        if label:
            break

    return label
