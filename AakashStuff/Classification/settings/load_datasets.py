import csv
import os
import pickle
from sklearn.utils import shuffle
from keras.datasets import mnist, cifar10
import fiftyone as fo
import cv2
import numpy as np
from sklearn.utils import shuffle
import skimage.io
import skimage.transform
import skimage.color
from sklearn.utils import shuffle

scaleFactor = 4


def load_data_garbage_classification():
    signs = []
    with open('Garbageclassification/classnames.csv', 'r') as csvfile:
        signnames = csv.reader(csvfile, delimiter=',')
        next(signnames, None)
        for row in signnames:
            signs.append(row[1])
        csvfile.close()

    # Step 2, dataset info
    X_data = []
    y_data = []
    for directory in os.walk("Garbageclassification"):
        for file in directory[2]:
            if "jpg" in file.lower():
                if "cardboard" in file:
                    y_data.append(0)
                elif "glass" in file:
                    y_data.append(1)
                elif "metal" in file:
                    y_data.append(2)
                elif "paper" in file:
                    y_data.append(2)
                elif "plastic" in file:
                    y_data.append(3)
                elif "trash" in file:
                    y_data.append(4)
                img = skimage.io.imread(f"{directory[0]}\\{file}")
                scaled = skimage.transform.resize(img, (img.shape[1] // scaleFactor, img.shape[0] // scaleFactor), anti_aliasing=False)
                scaled = skimage.color.rgb2gray(scaled)
                #
                # cv2.imshow("img", scaled)
                X_data.append(scaled)
                # cv2.waitKey(0)
                # print(file)
    X_data, y_data = shuffle(X_data, y_data)
    X_data, y_data = shuffle(X_data, y_data)
    X_train = X_data[:int(len(X_data) * 0.9)]
    X_test = X_data[int(len(X_data) * 0.9):]
    y_train = y_data[:int(len(y_data) * 0.9)]
    y_test = y_data[int(len(y_data) * 0.9):]

    X_train = np.array(X_train)
    X_test = np.array(X_test)
    y_train = np.array(y_train)
    y_test = np.array(y_test)
    return (X_train, y_train), (X_test, y_test), (X_test, y_test), signs
