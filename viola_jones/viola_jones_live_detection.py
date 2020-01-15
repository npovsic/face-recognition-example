import cv2
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

i = 0

while True:
    ret, img = cap.read()
    
    frames+=1

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    detected_faces = face_detection.detect_faces(gray)

    for (x, y, w, h) in detected_faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

    cv2.imshow('video', img)

    k = cv2.waitKey(30) & 0xff

    if k == 27:  # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()
