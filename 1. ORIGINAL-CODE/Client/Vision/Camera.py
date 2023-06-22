import cv2

class Camera:
    def __init__(self, cameraID):
        self.cap = cv2.VideoCapture(cameraID)

    def frame(self):
        ret, frame = self.cap.read()
        if ret:
            return frame
        else:
            return None
    
    def release(self):
        self.cap.release()
        # cv2.destroyAllWindows()