import cv2
import time
from stream import VideoStream


class FrameCapture:
    def __init__(self, address):
        self.address = address
        self.stream = None
        self.frame = None

    def connect(self):
        self.stream = VideoStream(self.address).start()
        time.sleep(1)

    def display_stream(self):
        cv2.namedWindow('Stream', cv2.WINDOW_NORMAL)
        while 1:
            self.frame = self.stream.read()
            if self.frame is None:
                print('Frame is none')
                break
            if cv2.waitKey(10) != cv2.waitKey(27):
                break
            cv2.imshow('Stream', self.frame)
        cv2.destroyAllWindows()
        self.stream.stop()
