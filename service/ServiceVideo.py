import sys
sys.path.append('../')
# from concurrent.futures import thread
import threading
import time
from controller.camera import Camera

class ServiceVideo:
  def __init__(self):
    self.isRecording = False
    # self.event = threading.Event()
    self.camera = Camera()

  def start(self):
    thread_video = threading.Thread(target=self.run)
    # thread_listening = threading.Thread(target=self.stopListening, args = (self.event, ))
    # thread_listening.start()
    thread_video.start()

  def stop(self):
    # self.event.set()
    self.isRecording = False
    self.camera.close()

  def run(self):
    if self.camera.isActive:
      return
    self.isRecording = True
    self.camera.start()

    while self.isRecording:
      ret = self.camera.capture()
      if not ret:
        self.isRecording = False

  # def stopListening(self, event):
  #   event.wait()
  #   self.isRecording = False

  # def getMessage(self):
  #   return 'video'

if __name__ == '__main__':
  video = ServiceVideo()
  video.start()
  print('video1 started')
  time.sleep(5)
  video.stop()
  print('video1 stopped')
  print('simulation done')
