import RPi.GPIO as GPIO
from controller.run_pump import Pump
import threading
import time


PIN = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def isBeingPushed():
    return not GPIO.input(PIN) # pushed True / unpushed False
    
def buttonPushedEvent(event):
    event.wait()
    print('button pushed')
    event.clear()
    
event = threading.Event()

while True:
    if isBeingPushed():
        thread_button = threading.Thread(target=buttonPushedEvent, args=(event, ))
        thread_button.start()
        event.set()
        time.sleep(1)
        

