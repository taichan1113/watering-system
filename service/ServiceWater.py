import time
from controller.show_soilMoisture import CSMS12
from controller.run_pump import Pump

class ServiceWater:
  def __init__(self):
    self.isWatering = False
    self.soilMoisture = None
    self.wet = 50
  
  def serve(self):
    sensor = CSMS12()
    pump = Pump()
    start_time = time.time()

    while sensor.moisturePercentage() < self.wet:
      if time.time() - start_time > 10: # forcibly break 10 sec after pump start
        break

      if pump.isActivated:
        continue
      else:
        pump.start()
        self.isWatering = True
    
    pump.stop()
    self.isWatering = False
    self.soilMoisture = sensor.moisturePercentage()

  def getMessage(self):
    pub_msg = 'Done water at' + '\n' + f'Soil Moisture: {self.soilMoisture}'
    return pub_msg






