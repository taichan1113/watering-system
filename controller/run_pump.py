import RPi.GPIO as GPIO
import time

PIN_PUMP = 25

class Pump:
  def __init__(self):
    self.GPIO = GPIO
    self.GPIO.setmode(GPIO.BCM)
    self.GPIO.setup(PIN_PUMP, GPIO.OUT)
    self.isActivated = False

  def start(self):
    self.isActivated = True
    self.GPIO.output(PIN_PUMP, 1)

  def stop(self):
    self.GPIO.output(PIN_PUMP, 0)
    self.isActivated = False
    
  def close(self):
    self.GPIO.cleanup(PIN_PUMP)

  def runPump(self, sec):
    self.start()
    time.sleep(sec)
    self.stop()
    self.close()

if __name__ == "__main__":
  pump = Pump()
  pump.runPump(3)
