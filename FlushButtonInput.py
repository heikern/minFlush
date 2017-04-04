import RPi.GPIO as GPIO
import time

button = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def buttonState():
	return GPIO.input(button)


if __name__ == '__main__':
	while True:
	    input_state = GPIO.input(button)
	    if input_state == False:
	        print('Button Pressed')
	        time.sleep(1)