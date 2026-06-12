import cv2

cam = cv2.VideoCapture(0)


def capture_cam(cam=cam):
    if not cam.isOpened():
        raise RuntimeError("Could not found webcam")

    while True:
        ret, frame = cam.read()

        if not ret:
            break

        cv2.imshow("Airctl camera preview", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cam.release()
    cv2.destroyAllWindows()
