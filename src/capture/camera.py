# import cv2


# class Camera:
#     def __init__(self, index=0):
#         self.index = index
#         self.cam = None

#     def __enter__(self):
#         self.cam = cv2.VideoCapture(self.index)
#         if not self.cam.isOpened():
#             raise RuntimeError("Could not found webcam")
#         return self.cam

#     def __exit__(self, exc_type, exc_value, traceback):
#         if self.cam is not None:
#             self.cam.release()
#         cv2.destroyAllWindows()
from contextlib import contextmanager

import cv2


@contextmanager
def camera(index=0):
    cam = cv2.VideoCapture(index)

    if not cam.isOpened():
        raise RuntimeError("Could not find webcam")

    try:
        yield cam

    finally:
        cam.release()
        cv2.destroyAllWindows()
