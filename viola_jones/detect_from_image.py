import os
import time

from os import listdir
from os.path import isfile, join

import cv2
import numpy
from PIL import Image

import face_detection as face_detection

from pathlib import Path

IMAGES_FOLDER = Path.cwd().parent.joinpath("images")

images = [image for image in IMAGES_FOLDER.glob("*.png")]

for image in images:
    image_name = str(image).split("/")[-1]

    PIL_image = Image.open(image).convert('RGB')
    img = numpy.array(PIL_image)

    start = time.time()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    detected_faces = face_detection.detect_faces(gray)

    for (x, y, w, h) in detected_faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

    end = time.time()

    print(image_name, end - start)

    cv2.imshow(image_name, img)

while True:
    k = cv2.waitKey(30) & 0xff

    if k == 27:  # press 'ESC' to quit
        break

cv2.destroyAllWindows()
