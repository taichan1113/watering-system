# from controller.show_tempAndHumid import DHT22
# from controller.turnOn_led import ledOn

# GPIO_LED = 21

from ServiceEnvironment import ServiceEnvironment as Environment


class ServiceConductor:
  def __init__(self, recieve_message):
    self.recieve_message = recieve_message
    self.publish_message = 'no service'

  def conduct_service(self):
    if self.recieve_message == 'service=water':
      print('test water')
        
    elif self.message == 'service=environment':
      print('test environment')
      service = Environment()
      self.publish_message = service.serve()
        
    elif self.message == 'service=stream':
      print('test stream')
        
    else:
      print('no service')
    