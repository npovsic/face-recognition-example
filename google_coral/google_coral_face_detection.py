import os

from edgetpu.detection.engine import DetectionEngine

FACE_DETECTION_MODEL_PATH = os.path.normpath(
    os.path.join(
        os.getcwd(),
        "mobilenet_ssd_v2_face_quant_postprocess_edgetpu.tflite",
    )
)

face_detection_engine = DetectionEngine(FACE_DETECTION_MODEL_PATH)

confidence = 0.3
MAX_FACES = 30

def detect_faces(image):
    return face_detection_engine.detect_with_image(
        image,
        threshold=confidence,
        keep_aspect_ratio=True,
        relative_coord=False,
        top_k=MAX_FACES,
    )
