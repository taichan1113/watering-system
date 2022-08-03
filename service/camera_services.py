import sys
sys.path.append('../')
import time
from service.ServiceVideo import ServiceVideo
from service.youtube_live import YouTubeLive

class CameraServices:
    def __init__(self):
#         self.video = ServiceVideo()
        self.stream = YouTubeLive()
        self.message = ''
        # self.isActive = self.video.isRecording^self.stream.isStreaming # xor

    def serve(self):
        self.message = self.stream.toggle(self.video.isRecording)

    def offerVideo(self):
        if self.stream.isStreaming:
            self.stream.stop()
        video = ServiceVideo()
        video.start()
        self.message = 'movie url will be here'
        
        return video.stop


    def getMessage(self):
        return self.message

if __name__ == "__main__":
    cs = CameraServices()
    handler = cs.offerVideo()
    print(cs.getMessage())
    time.sleep(10)
    handler()
