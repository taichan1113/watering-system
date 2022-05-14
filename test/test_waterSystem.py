import time
import subprocess
import RPi.GPIO as GPIO
from gpiozero import MCP3008

from run_pump import runPump
from show_soilMoisture import humidityPercentage
from turnOn_led import ledOn

if __name__ == "__main__":
    # setup pump
    GPIO.setmode(GPIO.BCM)
    GPIO_PUMP = 17
    GPIO_LED = 21

    # setup humidity
    sensor = MCP3008(channel = 0)

    try:
        while True:
            hum = humidityPercentage(sensor, Vref=3.3, dry=290, water=130)
            if hum < 80:
                ledOn(3, GPIO_LED)
                runPump(3, GPIO_PUMP)
                print('dry')
                
            
            time.sleep(3)
                
    except: KeyboardInterrupt
    subprocess.call('clear')
