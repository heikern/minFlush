import RPi.GPIO as GPIO
import time

lightPin = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(lightPin, GPIO.OUT)
GPIO.output(lightPin, GPIO.HIGH)

def changeLightState(state):
	if state == 'off':
		GPIO.output(lightPin, GPIO.HIGH)
                #GPIO.setup(lightPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	elif state == 'on':
		GPIO.output(lightPin, GPIO.LOW)
	else:
		GPIO.output(lightPin, GPIO.HIGH)
		print 'error in state'

