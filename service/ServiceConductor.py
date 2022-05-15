from controller.show_tempAndHumid import DHT22
from controller.turnOn_led import ledOn

GPIO_LED = 21

def conduct(message):
  print(message)
  pub_msg = 'this message should be overwritten'

  if message == 'service=water':
    print('test water')
    ledOn(1, GPIO_LED)
      
  elif message == 'service=environment':
    print('test environment')
    sense = DHT22()
    temp = sense.get_temperature()
    hum = sense.get_humidity()
    pub_msg = f'Temperature: {temp}' + '\n' + f'Humidity: {hum}'
      
  elif message == 'service=stream':
    print('test stream')
    ledOn(1, GPIO_LED)
      
  else:
    ledOn(1, GPIO_LED)

  return pub_msg
    