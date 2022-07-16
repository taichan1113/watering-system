import time
import subprocess
import os
import signal

class YouTubeLive():
    def __init__(self):
        self.isStreaming = False
        # self.DEV_ID = 0
        # self.WIDTH = 640
        # self.HEIGHT = 480
        # self.FPS = 30
        self.cmd = "/home/pi/Documents/Live/Live_v2.sh"
        
    def start(self):
        self.isStreaming = True
#         self.proc = subprocess.Popen("exec " + self.cmd, shell=True)
        self.proc = subprocess.Popen(self.cmd, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
        
    def stop(self):
#         self.proc.kill()
        os.killpg(os.getpgid(self.proc.pid), signal.SIGTERM)
        self.isStreaming = False
        
if __name__ == '__main__':
    live = YouTubeLive()
    live.start()
    time.sleep(20)
    live.stop()
    exit()


