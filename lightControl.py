import RPi.GPIO as GPIO
import time

lightPin = [5,6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(lightPin[0], GPIO.OUT)
GPIO.setup(lightPin[1], GPIO.OUT)


GPIO.output(lightPin[0], GPIO.LOW)
GPIO.output(lightPin[1], GPIO.LOW)

def changeLightState(pin,state):
	if state == 'off':
		GPIO.output(lightPin[pin], GPIO.LOW)
	elif state == 'on':
		GPIO.output(lightPin[pin], GPIO.HIGH)
	else:
		GPIO.output(pin, GPIO.LOW)
		print 'error in state'

