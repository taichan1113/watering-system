class ServiceVideo:
  def __init__(self):
    self.isRecording = False

  def serve(self):
    return

  def start(self):
    return

  def stop(self):
    return

  

  def getMessage(self):
    return 'video'

if __name__ == "__main__":
  video = ServiceVideo()
  video.start()
  video.stop()