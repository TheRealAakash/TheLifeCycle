import ClassifierModel
import numpy as np
import os
import random
from PIL import Image
import cv2
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

organic_path = r"D:\OneDrive\ByteKode Hackathon\TrashClassifier\Dataset 2\archive\DATASET\TEST\O"
recycle_path = r"D:\OneDrive\ByteKode Hackathon\TrashClassifier\Dataset 2\archive\DATASET\TEST\R"

images = []
labels = []
input_shape = ClassifierModel.get_dimension()
batch_size = ClassifierModel.get_batch_size()

def resize_image(im_path):
    success = False
    im_array = plt.imread(f"{im_path}")
    im_array = cv2.resize(im_array, input_shape)
    if im_array.shape == ClassifierModel.get_shape():
        images.append(im_array)
        success = True
    # print(f"shape: {im_array.shape}")
    return success


for file in os.listdir(organic_path):
    if file.endswith(".jpg"):
        if resize_image(organic_path + "\\" + file):
            labels.append(0)

for file in os.listdir(recycle_path):
    if file.endswith(".jpg"):
        if resize_image(recycle_path + "\\" + file):
            labels.append(1)

# print(f"array shape {images[0]}")

x_train, x_test, y_train, y_test = train_test_split(images, labels, test_size = 0.2, random_state = 34)

print(f"x_train: {len(x_train)}; y_train: {len(y_train)}")
print(f"x_test: {len(x_test)}; y_test: {len(y_test)}")

# x_train = []
# x_test = []
# batch = []
#
# for image in x_train:
#     batch.append(image)
#     if len(batch) == batch_size:
#         normalized_batch = np.array(batch) / 255.0
#         x_train.append(normalized_batch)
#         batch = []
#
#
# print(f"x_train: {len(x_train)}; y_train: {len(y_train)}")
# print(f"x_test: {len(x_test)}; y_test: {len(y_test)}")
# x_train = np.dstack(x_train) / 255.0
# x_test = np.dstack(x_test) / 255.0

all_same = True
prev_shape = x_train[0].shape
for i in x_train:
    # print(f"shape: {i.shape}")
    if i.shape != prev_shape:
        all_same = False
        break

print(f"all_same = {all_same}")

x_train = np.asarray(x_train)
x_test = np.asarray(x_test)
y_train = np.array(y_train)
y_test = np.array(y_test)

model, history = ClassifierModel.train_model(x_train, y_train, x_test, y_test)
model.save("type-classifier3.model")

val_y_preds = model.predict(x_train)
for i in range(len(val_y_preds)):
    val_y_preds[i] = np.argmax(val_y_preds[i])

val_y = y_train

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(10)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()

print(f"Val Accuracy Score: {accuracy_score(val_y, val_y_preds)*100}%")

c = confusion_matrix(val_y, val_y_preds)
error_rate = (c[0][1] + c[1][0]) / (c[0][0] + c[0][1] + c[1][0] + c[1][1])
print(f"The error rate is {error_rate * 100} %")
print(f"Confusion Matrix: \n{c}")

prf = precision_recall_fscore_support(val_y, val_y_preds)

print('Precision:', prf[0][1])
print('Recall:', prf[1][1])
print('F-Score:', prf[2][1])