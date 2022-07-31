import time
from service.ServiceVideo import ServiceVideo
from service.youtube_live import YouTubeLive


class CameraServices:
    def __init__(self):
        self.video = ServiceVideo()
        self.stream = YouTubeLive()
        # self.isActive = self.video.isRecording^self.stream.isStreaming # xor

    def serve(self):
        self.stream.toggle(self.video.isRecording)

    def getMessage(self):
        return 'test'
