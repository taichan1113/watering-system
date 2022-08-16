import sys
sys.path.append('../')
from service.ServiceEnvironment import ServiceEnvironment
from service.ServiceWater import ServiceWater
from service.camera_services import CameraServices

class ServiceConductor:
  def __init__(self):
    # self.recieve_message = recieve_message
    self.publish_message = 'no service'
    self.environment = ServiceEnvironment()
    self.camera = CameraServices()
    self.water =ServiceWater(self.camera)

  def conduct_service(self, recieve_message):
    if recieve_message == 'service=water':
      print('test water')
      service = self.water
        
    elif recieve_message == 'service=environment':
      print('test environment')
      service = self.environment
        
    elif recieve_message == 'service=stream':
      print('test stream')
      service = self.camera
        
    else:
      print('no service')
      return
    
    try:
        service.serve()
        self.publish_message = service.getMessage()
    except:
        print('error')
    
if __name__ == "__main__":
    sc = ServiceConductor()
    sc.conduct_service('service=water')
    print(sc.publish_message)
    