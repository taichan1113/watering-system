import sys
sys.path.append('../')
# from concurrent.futures import thread
import boto3
import threading
import time
from controller.camera import Camera
from dotenv import load_dotenv
import os

from linebot import (
   LineBotApi, WebhookHandler
) 
from linebot.exceptions import InvalidSignatureError
from linebot.models import VideoSendMessage

load_dotenv('./.env')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
MY_LINE_USER_ID = os.environ["MY_LINE_USER_ID"]
MY_CHANNEL_ACCESS_TOKEN = os.environ["MY_CHANNEL_ACCESS_TOKEN"]

line_bot_api = LineBotApi(MY_CHANNEL_ACCESS_TOKEN)

class ServiceVideo:
  def __init__(self):
    self.isRecording = False
    # self.event = threading.Event()
    self.camera = Camera()
    self.awsclient = boto3.client(
      's3',
      aws_access_key_id = AWS_ACCESS_KEY_ID,
      aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
      region_name = 'ap-northeast-1'
    )

  def start(self):
    thread_video = threading.Thread(target=self.run)
    # thread_listening = threading.Thread(target=self.stopListening, args = (self.event, ))
    # thread_listening.start()
    thread_video.start()

  def stop(self):
    # self.event.set()
    self.isRecording = False
    self.camera.close()
    Filename = self.camera.path
    Bucket = 'taichi-home-iot-1113'
    Key = 'uploaded/watering.mp4'
    self.awsclient.upload_file(Filename, Bucket, Key)
    videoURL = 'https://taichi-home-iot-1113.s3.ap-northeast-1.amazonaws.com/uploaded/watering.mp4'
    previewURL = 'https://taichi-home-iot-1113.s3.ap-northeast-1.amazonaws.com/uploaded/shizukun.PNG'

    line_bot_api.push_message(MY_LINE_USER_ID, 
    VideoSendMessage(
      original_content_url=videoURL,
      preview_image_url=previewURL))

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
