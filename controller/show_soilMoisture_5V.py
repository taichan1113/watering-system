import time
from gpiozero import MCP3008

class CSMS12:
  def __init__(self):
    self.Vref = 5.0
    self.dry = 435
    self.water = 200
    self.ADC = MCP3008(channel=0)
  
  def moisture(self):
    return (self.ADC.value * self.Vref * 100)

  def moisturePercentage(self):
    moisture_percentage = round((1 - (self.moisture() - self.water) / (self.dry - self.water)) * 100, 1)
    return moisture_percentage

if __name__ == "__main__":
  sensor = CSMS12()
  print('system start')
  while True:
    try:
      print(sensor.moisturePercentage())
      time.sleep(1)
    except KeyboardInterrupt:
      print('system end')
      break
    

    

