from service.ServiceEnvironment import ServiceEnvironment as Environment
from service.ServiceWater import ServiceWater as Water

class ServiceConductor:
  def __init__(self, recieve_message):
    self.recieve_message = recieve_message
    self.publish_message = 'no service'

  def conduct_service(self):
    if self.recieve_message == 'service=water':
      print('test water')
      service = Water()
        
    elif self.recieve_message == 'service=environment':
      print('test environment')
      service = Environment()
        
    elif self.recieve_message == 'service=stream':
      print('test stream')
        
    else:
      print('no service')
      return
    
    service.serve()
    self.publish_message = service.getMessage()
    