import RPi.GPIO as GPIO
import time

valvePin = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(valvePin, GPIO.OUT)

# initialise
GPIO.output(valvePin, GPIO.LOW)


try:
    counter = 0
    while True:
    	if counter%2==0:
    		GPIO.output(valvePin, GPIO.LOW)
    	else:
    		GPIO.output(valvePin, GPIO.HIGH)
	counter+=1
    	time.sleep(1)
        
except KeyboardInterrupt:
    GPIO.cleanup() # cleanup all GPIO
