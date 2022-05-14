import RPi.GPIO as GPIO
import time
import Adafruit_Python_DHT as DHT

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

sensor = dht11.DHT11(pin=14)

try:
    while True:
        result = sensor.read()
        if result.is_valid():
            print("Temperature: %-3.1f C" % result.temperature)
            print("Humidity: %-3.1f %%" % result.humidity)
        else:
            print("result invalid")
            print("Temperature: %-3.1f C" % result.temperature)
            print("Humidity: %-3.1f %%" % result.humidity)

        time.sleep(1)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()