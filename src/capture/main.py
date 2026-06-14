import cv2

from src.capture.camera import camera
from src.tracker.main import tracker


cam = cv2.VideoCapture(0)


def capture_cam(cam=cam):
    with camera() as cam:
        while True:
            ret, frame = cam.read()

            if not ret:
                break
            frame = tracker.detect(frame)
            cv2.imshow("Airctl camera preview", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
