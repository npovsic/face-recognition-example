import cv2
import viola_jones.viola_jones_face_detection as face_detection

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    detected_faces = face_detection.detect_faces(gray)

    for (x, y, w, h) in detected_faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

    cv2.imshow('video', img)

    fps = cap.get(cv2.CAP_PROP_FPS)
    print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))

    k = cv2.waitKey(30) & 0xff

    if k == 27:  # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()
