from controller.show_tempAndHumid import DHT22

class ServiceEnvironment:
  def __init__(self):
    self.temperature = None
    self.humidity = None
    self.soilMoisture = None
    self.sensor = DHT22()
  
  def serve(self):
    self.temperature = self.sensor.get_temperature()
    self.humidity = self.sensor.get_humidity()

    pub_msg = f'Temperature: {self.temperature}' + '\n' + f'Humidity: {self.humidity}' + '\n' + f'Soil Moisture: {self.soilMoisture}'
    return pub_msg


