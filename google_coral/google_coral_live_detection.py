import cv2
import threading
from PIL import Image
import face_detection as face_detection

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


class GoogleCoralLiveDetection:
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