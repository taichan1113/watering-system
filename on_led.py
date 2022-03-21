import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_LED = 21

def ledOn(sec, num_gpio):
    GPIO.setup(num_gpio, GPIO.OUT)
    
    GPIO.output(num_gpio, 1)
    time.sleep(sec)
    GPIO.output(num_gpio, 0)
    
    GPIO.cleanup(num_gpio)
    return

if __name__ == "__main__":
    ledOn(1, GPIO_LED)