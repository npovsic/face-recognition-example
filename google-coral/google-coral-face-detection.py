import cv2
import os
from PIL import Image

from edgetpu.detection.engine import DetectionEngine

FACE_DETECTION_MODEL_PATH = os.path.normpath(
    os.path.join(
        os.getcwd(),
        "mobilenet_ssd_v2_face_quant_postprocess_edgetpu.tflite",
    )
)

face_detection_engine = DetectionEngine(FACE_DETECTION_MODEL_PATH)

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

confidence = 0.3
MAX_FACES = 10

while True:
    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    rgb_array = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    frame_as_image = Image.fromarray(rgb_array)

    processed_frame = frame_as_image

    detected_faces = face_detection_engine.detect_with_image(
        processed_frame,
        threshold=confidence,
        keep_aspect_ratio=True,
        relative_coord=False,
        top_k=MAX_FACES,
    )

    for face in detected_faces:
        bounding_box = face.bounding_box.flatten().astype("int")

        (x1, y1, x2, y2) = bounding_box

        width = x2 - x1
        height = y2 - y1

        cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
        roi_gray = gray[y1:y2, x1:x2]
        roi_color = img[y1:y2, x1:x2]

        print(bounding_box)

    cv2.imshow('video', img)

    fps = cap.get(cv2.CAP_PROP_FPS)
    print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))

    k = cv2.waitKey(30) & 0xff

    if k == 27:  # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()
