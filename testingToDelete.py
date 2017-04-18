import RPi.GPIO as GPIO
import time

lightPin = 21


GPIO.setmode(GPIO.BCM)
GPIO.setup(lightPin, GPIO.OUT)
GPIO.output(lightPin, GPIO.HIGH)

while True:
    time.sleep(2)
    GPIO.output(lightPin, GPIO.HIGH)
    print 'GPIO LOW'
    time.sleep(2)
    GPIO.output(lightPin, GPIO.LOW)
    print 'GPIO HIGH'
