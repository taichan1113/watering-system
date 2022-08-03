import time
from service.ServiceVideo import ServiceVideo
from service.youtube_live import YouTubeLive


class CameraServices:
    def __init__(self):
        self.video = ServiceVideo()
        self.stream = YouTubeLive()
        self.message = ''
        # self.isActive = self.video.isRecording^self.stream.isStreaming # xor

    def serve(self):
        self.message = self.stream.toggle(self.video.isRecording)

    def offerVideo(self):
        if self.stream.isStreaming:
            self.stream.stop()
        
        self.video.start()
        self.message = 'movie url will be here'
        
        return self.video.stop


    def getMessage(self):
        return self.message
