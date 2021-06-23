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

    def take_size(self):
        return [self.stream.get(cv2.CAP_PROP_FRAME_WIDTH), self.stream.get(cv2.CAP_PROP_FRAME_HEIGHT)]

    def take_frame(self):
        return self.frame

    def take_fps(self):
        return self.stream.get(cv2.CAP_PROP_FPS)

    def take_pos(self):
        return [self.stream.get(cv2.CAP_PROP_POS_MSEC), self.stream.get(cv2.CAP_PROP_POS_FRAMES)]

    def show_frame(self):
        if self.frame is not None:
            cv2.imshow('stream', self.frame)
            cv2.waitKey(self.FPS_MS)

    def is_open(self):
        return self.stream.isOpened() and self.status
