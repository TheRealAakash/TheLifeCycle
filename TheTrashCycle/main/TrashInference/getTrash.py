import os

import cv2
import imageio
import numpy as np

from .mrcnn import model as modellib
from .trash import trash
import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()

TRASH_WEIGHTS_PATH = "weights/mask_rcnn_trash_0200_030519_large.h5"  # the best
print('Weights being used: ', TRASH_WEIGHTS_PATH)

"""
    test everything
"""

ROOT_DIR = os.getcwd()
MODEL_DIR = os.path.join(ROOT_DIR, "logs")
COCO_MODEL_PATH = os.path.join(ROOT_DIR, "weights\\mask_rcnn_trash_0200_030519_large.h5")

config = trash.TrashConfig()
TRASH_DIR = 'trash'


class InferenceConfig(config.__class__):
    # Run detection on one image at a time
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1


config = InferenceConfig()
config.display()

DEVICE = "/cpu:0"  # /cpu:0 or /gpu:0
dataset = trash.TrashDataset()
dataset.load_trash(TRASH_DIR, "val")
dataset.prepare()
print("Images: {}\nClasses: {}".format(len(dataset.image_ids), dataset.class_names))
with tf.device(DEVICE):
    model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=config)

weights_path = "/home/aakash/Documents/Projects/Python/TheTrashCycle/TheTrashCycle/main/TrashInference/weights/mask_rcnn_trash_0200_030519_large.h5"
model.load_weights(weights_path, by_name=True)
model.keras_model._make_predict_function()


def infer(frame):
    results = model.detect([frame], verbose=0)
    r = results[0]
    # frame = display_instances(
    #     frame, r['rois'], r['masks'], r['class_ids'], dataset.class_names, r['scores']
    # )
    return frame, r




def main():
    USE_OBS = False
    if not USE_OBS:
        capture = cv2.VideoCapture(0)
    else:
        obs_reader = imageio.get_reader('<video2>')

    # these 2 lines can be removed if you dont have a 1080p camera.
    # capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    # capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    while True:
        if not USE_OBS:
            ret, frame = capture.read()
        else:
            frame = obs_reader.get_next_data()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if frame is None:
            print("frame was none")
            continue
        cv2.imshow("FrameOriginal", frame)
        frame, r = infer(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
