import cv2, time
from threading import Thread


class VideoStream():
    def __init__(self, stream_url=0):
        self.stream = cv2.VideoCapture(stream_url)
        self.stream.set(cv2.CAP_PROP_BUFFERSIZE, 2)

        # The first variable returns True if frame is not None
        (self.status, self.frame) = self.stream.read()

        # Инициализация значения FPS
        self.FPS = 1 / 30
        self.FPS_MS = int(self.FPS * 1000)

        # Инициализация потока
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        while True:
            if self.is_open():
                (self.status, self.frame) = self.stream.read()
            time.sleep(self.FPS)

    def take_frame(self):
        return self.frame

    def show_frame(self):
        cv2.imshow('stream', self.frame)
        cv2.waitKey(self.FPS_MS)

    def is_open(self):
        return self.stream.isOpened() and self.status
