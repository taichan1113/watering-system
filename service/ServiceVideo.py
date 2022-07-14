# from concurrent.futures import thread
import threading
import time
from controller.camera import Camera

class ServiceVideo:
  def __init__(self):
    self.isRecording = False
    self.event = threading.Event()

  def serve(self):
    return

  def start(self):
    thread_video = threading.Thread(target=self.run)
    thread_listening = threading.Thread(target=self.stopListening, args = (self.event, ))
    thread_listening.start()
    thread_video.start()

  def stop(self):
    self.event.set()

  def run(self):
    self.isRecording = True
    num = 0
    while self.isRecording:
      # self.capture() will be here
      print(num)
      num = num + 1
      time.sleep(0.5)

  def stopListening(self, event):
    event.wait()
    self.isRecording = False

  def getMessage(self):
    return 'video'

if __name__ == '__main__':
  video = ServiceVideo()
  video.start()
  time.sleep(3)
  video.stop()
  print('simulation done')
