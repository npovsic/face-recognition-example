import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

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

interval = set_interval(flush_frames, 1)

while True:
    ret, img = cap.read()

    frames+=1

    cv2.imshow('video', img)

    k = cv2.waitKey(30) & 0xff

    if k == 27:  # press 'ESC' to quit
        break


interval.cancel()
cap.release()
cv2.destroyAllWindows()
