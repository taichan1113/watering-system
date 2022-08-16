import sys
sys.path.append('../')
import time
from controller.show_soilMoisture_5V import CSMS12
from controller.run_pump import Pump
from service.camera_services import CameraServices

class ServiceWater:
  def __init__(self, camera_service):
    self.isWatering = False
    self.soilMoisture = None
    self.wet = 50
    self.camera_service = camera_service
  
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
        # video_stop_handler = self.camera_service.offerVideo()
        self.camera_service.pauseStreamAndStartVideo()
        pump.start()
        self.isWatering = True
    
    pump.stop()
    self.camera_service.stopVideoAndContinueStream()
    # video_stop_handler()


    self.isWatering = False
    self.soilMoisture = sensor.moisturePercentage()
    pump.close()

  def getMessage(self):
    pub_msg = 'Done water at' + '\n' + f'Soil Moisture: {self.soilMoisture}'
    return pub_msg

if __name__ == "__main__":
    camera_services = CameraServices()
    service = ServiceWater(camera_services)
    service.serve()
