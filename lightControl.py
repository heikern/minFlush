import RPi.GPIO as GPIO
import time

lightPin = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(lightPin, GPIO.OUT)
GPIO.output(lightPin, GPIO.LOW)

def changeLightState(state):
	if state == 'off':
		GPIO.output(lightPin, GPIO.LOW)
	elif state == 'on':
		GPIO.output(lightPin, GPIO.HIGH)
	else:
		GPIO.output(lightPin, GPIO.LOW)
		print 'error in state'

