import cv2
import threading

import face_detection as face_detection


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


class ViolaJonesLiveDetection:
    def __init__(self, width, height):
        self.fps = 0

        self.width = width
        self.height = height

        self.cap = None

        self.timer = None

        self.capture = False

    def start(self):
        self.capture = True

        self.fps = 0

        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, self.width)
        self.cap.set(4, self.height)

        self.timer = set_interval(self.flush_frames, 1)

        while self.capture:
            ret, img = self.cap.read()

            self.fps += 1

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            detected_faces = face_detection.detect_faces(gray)

            for (x, y, w, h) in detected_faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

            cv2.imshow('video', img)

            cv2.waitKey(1)

    def flush_frames(self):
        print("Frames per second: {0}".format(self.fps))

        self.fps = 0

    def destroy(self):
        if self.cap is None:
            return

        self.capture = False

        self.cap.release()

        self.cap = None

        cv2.destroyWindow('video')

