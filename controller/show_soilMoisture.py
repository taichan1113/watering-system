import time
from gpiozero import MCP3008

class CSMS12:
  def __init__(self):
    self.Vref = 3.3
    self.dry = 290 # sensor max 283
    self.water = 130 # sensor min 133
    self.ADC = MCP3008(channel=0)

  def moisturePercentage(self):
    moisture = self.ADC.value * self.Vref * 100
    moisture_percentage = round((1 - (moisture - self.water) / (self.dry - self.water)) * 100, 1)
    return moisture_percentage

if __name__ == "__main__":
  sensor = CSMS12()
  while True:
    moist = sensor.moisturePercentage()
    if (moist >= 0 and moist < 25):
        print(f'very dry : {moist}%')
    elif (moist >= 25 and moist < 50):
        print(f'dry : {moist}%')
    elif (moist >= 50 and moist < 75):
        print(f'wet : {moist}%')
    elif (moist >= 75 and moist <= 100):
        print(f'very wet : {moist}%')

    time.sleep(1)
