import time
import adafruit_dht
from board import D24

class DHT22:
    def __init__(self, pin=D24, max_retry=5):
        self.dht22 = adafruit_dht.DHT22(pin, use_pulseio=False)
        self.temperature = None
        self.humidity = None
        
        retry = 0
        while not self.is_available():
            print('Trying to get proper data...')
            retry += 1
            if retry >= max_retry:
                raise RuntimeError('Couldn\'t get sensor data while retrying.')
            
            time.sleep(1)
        
    def is_available(self):
        self.temperature = self.get_temperature()
        self.humidity = self.get_humidity()
        if self.temperature and self.humidity:
            return True
        
        return False
        
    def get_temperature(self):
        try:
            self.temperature = self.dht22.temperature
        except RuntimeError:
            # Check sum failed or insufficient data.
            pass
        return self.temperature
    
    def get_humidity(self):
        try:
            self.humidity = self.dht22.humidity
        except RuntimeError:
            # Check sum failed or insufficient data.
            pass
        return self.humidity
    
if __name__ == '__main__':
    sense = DHT22()
    
    for i in range(3):
        temp = sense.get_temperature()
        hum = sense.get_humidity()
        
        print(f'====={time.ctime()}=====')
        print(f'Temperature: {temp}')
        print(f'Humidity: {hum}')
        
        time.sleep(1)