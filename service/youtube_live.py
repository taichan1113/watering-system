import time
import subprocess
import os
import signal


class YouTubeLive():
    def __init__(self):
        self.isStreaming = False
        self.cmd = "../controller/Live_v2.sh"
        self.url = "https://youtu.be/EI8UbbKIloE"

    def start(self):
        self.isStreaming = True
#         self.proc = subprocess.Popen("exec " + self.cmd, shell=True)
        self.proc = subprocess.Popen(
            self.cmd, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)

    def stop(self):
#         self.proc.kill()
        os.killpg(os.getpgid(self.proc.pid), signal.SIGTERM)
        self.isStreaming = False

    def toggle(self, guard):
        if self.isStreaming:
            self.stop()
            return 'stream stopped'
        elif not self.isStreaming:
            while guard:
                time.sleep(1)
            self.start()
            return 'stream start at ' +  self.url
        
if __name__ == '__main__':
    live = YouTubeLive()
    live.start()
    time.sleep(20)
    live.stop()
    exit()


