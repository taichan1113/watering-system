import RPi.GPIO as GPIO
from controller.run_pump import Pump
import threading
import time

class Button():
    def __init__(self):
        self.PIN = 19
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.toggle = False
        self.button_has_pushed = False
            
    def isButtonPushed(self):
        return not GPIO.input(self.PIN) # pushed True / unpushed False
    
    def buttonPushedEvent(self):
        while True:
            if self.isButtonPushed() and not self.button_has_pushed:                
                self.toggle = not self.toggle
                self.button_has_pushed = True
                
            elif not self.isButtonPushed() and self.button_has_pushed:
                self.button_has_pushed = False

if __name__ == '__main__':
    button = Button()
    pump = Pump()

    thread_button = threading.Thread(target=button.buttonPushedEvent)
    thread_button.start()
    while True:
        try:
            if button.toggle == True and not pump.isActivated:
                pump.start()
            if button.toggle == False and pump.isActivated:
                pump.stop()
        except KeyboardInterrupt:
            pump.stop()
            pump.close()