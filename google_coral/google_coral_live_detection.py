import cv2
from PIL import Image
import face_detection as face_detection

image_dimensions = {
    "width": 1280,
    "height": 720
}

cap = cv2.VideoCapture(0)
cap.set(3, image_dimensions["width"])
cap.set(4, image_dimensions["height"])

frames = 0

def flush_frames():
    global frames
    
    print("Frames per second: {0}".format(frames))
    
    frames = 0

import threading

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

set_interval(flush_frames, 1)

while True:
    ret, img = cap.read()
    
    frames+=1

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    rgb_array = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(rgb_array)

    detected_faces = face_detection.detect_faces(image)

    for face in detected_faces:
        bounding_box = face.bounding_box.flatten().astype("int")

        (x1, y1, x2, y2) = bounding_box

        width = x2 - x1
        height = y2 - y1

        cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
        roi_gray = gray[y1:y2, x1:x2]
        roi_color = img[y1:y2, x1:x2]

    cv2.imshow('video', img)
    
    k = cv2.waitKey(30) & 0xff

    if k == 27:  # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()
