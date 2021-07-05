import numpy as np
import cv2
import skimage
import skimage.io
import keras
from keras.callbacks import ModelCheckpoint
from keras.layers import Conv2D, Flatten, MaxPooling2D, Dense, Dropout
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img, array_to_img
import random, os, glob
import matplotlib.pyplot as plt

mainModel = None
filepath = "trained_model.h5"

img_list = glob.glob(os.path.join(filepath, '*/*.jpg'))

len(img_list)


def getGenerator():
    train = ImageDataGenerator(horizontal_flip=True, vertical_flip=True, validation_split=0.1, rescale=1. / 255,
                               shear_range=0.1, zoom_range=0.1,
                               width_shift_range=0.1,
                               height_shift_range=0.1, )
    test = ImageDataGenerator(rescale=1 / 255, validation_split=0.1)
    train_generator = train.flow_from_directory(filepath, target_size=(300, 300), batch_size=32,
                                                class_mode='categorical', subset='training')
    test_generator = test.flow_from_directory(filepath, target_size=(300, 300), batch_size=32,
                                              class_mode='categorical', subset='validation')
    labels = (train_generator.class_indices)
    labels = dict((v, k) for k, v in labels.items())
    return train_generator, test_generator, labels


def build_model():
    model = Sequential()

    model.add(Conv2D(32, (3, 3), padding='same', input_shape=(300, 300, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=2))
    model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=2))
    model.add(Conv2D(32, (3, 3), padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=2))
    model.add(Flatten())
    model.add(Dense(64, activation='relu'))
    model.add(Dense(6, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])
    return model


def train():
    train_generator, test_generator, labels = getGenerator()
    checkpoint1 = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
    callbacks_list = [checkpoint1]

    model = build_model()
    model.fit_generator(train_generator, epochs=100, steps_per_epoch=2276 // 32, validation_data=test_generator,
                        validation_steps=251 // 32, callbacks=callbacks_list)
    model.save_weights(filepath)


def loadModel():
    global mainModel
    mainModel = build_model()
    mainModel.load_weights(filepath)


classes = ["cardboard", "glass", "metal", "paper", "plastic", "trash"]


def predict(image):
    skimage.io.imsave("saved.png", image)
    test_image = keras.preprocessing.image.load_img("saved.png", target_size=(300, 300))
    test_image = keras.preprocessing.image.img_to_array(test_image) / 255
    test_image = np.expand_dims(test_image, axis=0)
    predicted_array = mainModel.predict(test_image)
    predicted_value = classes[np.argmax(predicted_array)]
    return predicted_value


if __name__ == '__main__':
    train()
