import sys
sys.path.append('../')
import time
from service.ServiceVideo import ServiceVideo
from service.youtube_live import YouTubeLive

class CameraServices:
    def __init__(self):
        self.video = ServiceVideo()
        self.stream = YouTubeLive()
        self.message = ''
        # self.isActive = self.video.isRecording^self.stream.isStreaming # xor
        self.isStreamPaused = False

    def serve(self):
        self.message = self.stream.toggle(self.video.isRecording)

    # def offerVideo(self):
    #     if self.stream.isStreaming:
    #         self.stream.stop()
    #     # video = ServiceVideo()
    #     self.video.start()
    #     self.message = 'movie url will be here'
        
    #     return self.video.stop

    def pauseStreamAndStartVideo(self):
        if self.stream.isStreaming:
            self.stream.stop()
            self.isStreamPaused = True
        # video = ServiceVideo()
        self.video.start()
    
    def stopVideoAndContinueStream(self):
        self.video.stop()
        self.message = 'movie url will be here'
        if self.isStreamPaused:
            self.stream.start()
            self.isStreamPaused = False

    def getMessage(self):
        return self.message

if __name__ == "__main__":
    cs = CameraServices()
    # handler = cs.offerVideo()
    cs.pauseStreamAndStartVideo()
    time.sleep(10)
    cs.stopVideoAndContinueStream()
    print(cs.getMessage())