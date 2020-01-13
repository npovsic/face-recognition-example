import os
import time

from os import listdir
from os.path import isfile, join

import cv2
import numpy
from PIL import Image, ImageOps

import google_coral.google_coral_face_detection as face_detection

from pathlib import Path

IMAGES_FOLDER = Path.cwd().parent.joinpath("images")

images = [image for image in IMAGES_FOLDER.glob("*.png")]

for image in images:
    image_name = str(image).split("/")[-1]

    PIL_image = Image.open(image)
    img = numpy.array(PIL_image)

    start = time.time()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    detected_faces = face_detection.detect_faces(PIL_image)

    for face in detected_faces:
        bounding_box = face.bounding_box.flatten().astype("int")

        (x1, y1, x2, y2) = bounding_box

        width = x2 - x1
        height = y2 - y1

        cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
        roi_gray = gray[y1:y2, x1:x2]
        roi_color = img[y1:y2, x1:x2]

    end = time.time()

    print(image_name, end - start)

    cv2.imshow(image_name, img)

while True:
    k = cv2.waitKey(30) & 0xff

    if k == 27:  # press 'ESC' to quit
        break

cv2.destroyAllWindows()
