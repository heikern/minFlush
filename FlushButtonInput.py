import RPi.GPIO as GPIO
import time

buttonPin = 21

# GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def buttonState():
	return GPIO.input(buttonPin)


if __name__ == '__main__':
	while True:
	    input_state = GPIO.input(buttonPin)
	    if input_state == False:
	        print('Button Pressed')
	        time.sleep(1)
