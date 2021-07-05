from . import getTrash
import skimage.io
import matplotlib.pyplot as plt
import cv2
import numpy as np
from . import wasteClassifier
from .TypeClassifier import classifier


# trashClassifier.loadModel()


# python main.py -m "classifyWaste.h5" -i "2.1.0" -o "1.15.0"
def random_colors(N):
    np.random.seed(1)
    colors = [tuple(255 * np.random.rand(3)) for _ in range(N)]
    return colors


def apply_mask(image, mask, color, alpha=0.5):
    """apply mask to image"""
    for n, c in enumerate(color):
        image[:, :, n] = np.where(
            mask == 1,
            image[:, :, n] * (1 - alpha) + alpha * c,
            image[:, :, n]
        )
    return image


def display_instances(image, boxes, masks, names, scores, showScores=False):
    """
        take the image and results and apply the mask, box, and Label
    """
    n_instances = boxes.shape[0]
    colors = random_colors(n_instances)

    if not n_instances:
        print('NO INSTANCES TO DISPLAY')

    for i, color in enumerate(colors):
        if not np.any(boxes[i]):
            continue

        y1, x1, y2, x2 = boxes[i]
        label = names[i]
        score = scores[i] if scores is not None else None
        if showScores:
            caption = '{} {:.2f}'.format(label, score) if score else label
        else:
            caption = '{}'.format(label) if score else label
        mask = masks[:, :, i]

        image = apply_mask(image, mask, color)
        image = cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
        image = cv2.putText(
            image, caption, (x1, y1), cv2.FONT_HERSHEY_COMPLEX, 0.7, color, 2
        )

    return image


def getClassesInFrame(frame, r):
    classes = []
    for region in r['rois']:
        y1, x1, y2, x2 = region
        im = frame[min(y1, y2):max(y1, y2), min(x1, x2):max(x1, x2)]
        label = wasteClassifier.predict(im)
        label += ", " # + classifier.get_class(im)

        print(label)
        classes.append(label)
    print(classes)
    return classes


def drawFrame(frame, r, classes):
    frame = display_instances(
        frame, r['rois'], r['masks'], classes, r['scores']
    )
    return frame


def renderFrame(frame):
    frame, r = getTrash.infer(frame)
    classes = getClassesInFrame(frame, r)
    frame = drawFrame(frame, r, classes)
    return frame, classes


def test():
    image_path = "test_images/trash_55.jpg"
    img = skimage.io.imread(image_path)
    frame, classes = renderFrame(img)
    cv2.imshow("f", frame)
    cv2.waitKey(0)
    image_path = "test_images/trash_58.jpg"
    img = skimage.io.imread(image_path)
    frame, classes = renderFrame(img)
    cv2.imshow("f", frame)
    cv2.waitKey(0)


if __name__ == '__main__':
    test()
