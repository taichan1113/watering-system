from controller.show_tempAndHumid import DHT22
from controller.show_soilMoisture_5V import CSMS12

class ServiceEnvironment:
  def __init__(self):
    self.temperature = None
    self.humidity = None
    self.soilMoisture = None
    self.sensor_temp_humid = DHT22()
    self.sensor_soilMoisture = CSMS12()
  
  def serve(self):
    self.temperature = self.sensor_temp_humid.get_temperature()
    self.humidity = self.sensor_temp_humid.get_humidity()
    self.soilMoisture = self.sensor_soilMoisture.moisturePercentage()

  def getMessage(self):
    pub_msg = f'Temperature: {self.temperature}' + '\n' + f'Humidity: {self.humidity}' + '\n' + f'Soil Moisture: {self.soilMoisture}'
    return pub_msg
