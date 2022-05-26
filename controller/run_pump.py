import RPi.GPIO as GPIO
import time

PIN_PUMP = 20

class Pump():
  def __init__(self):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_PUMP, GPIO.OUT)
    self.isActivated = False

  def start(self):
    self.isActivated = True
    GPIO.output(PIN_PUMP, 1)

  def stop(self):
    GPIO.output(PIN_PUMP, 0)
    GPIO.cleanup(PIN_PUMP)
    self.isActivated = False

  def runPump(self, sec):
    self.start()
    time.sleep(sec)
    self.stop()

if __name__ == "__main__":
  pump = Pump()
  pump.runPump(3)
