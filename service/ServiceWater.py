from controller.show_soilMoisture import CSMS12
from controller.run_pump import Pump

class ServiceWater:
  def __init__(self):
    self.isServiceRunning = False
    self.soilMoisture = None
    self.wet = 50
  
  def serve(self):
    sensor = CSMS12()
    pump = Pump()

    while sensor.moisturePercentage() < self.wet:
      if pump.isActivated:
        continue
      else:
        pump.start()
        self.isServiceRunning = True
    
    pump.stop()
    self.isServiceRunning = False
    self.soilMoisture = sensor.moisturePercentage()

  def getMessage(self):
    pub_msg = 'Done water at' + '\n' + f'Soil Moisture: {self.soilMoisture}'
    return pub_msg






