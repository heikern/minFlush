import RPi.GPIO as GPIO
import time

# pin definition
# input pin
switchPin = 21
#output pin
lightPin = 26
# note. relay pin is active low
relayPin = 22
ldrPin = 0



# Setup GPIO MODE
GPIO.setmode(GPIO.BCM)
GPIO.setup(switchPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(lightPin, GPIO.OUT)
GPIO.setup(relayPin, GPIO.OUT)


# Set initial state for LED
GPIO.output(lightPin, GPIO.LOW)
GPIO.output(relayPin, GPIO.LOW)

raw_input("wanna start?")

GPIO.output(relayPin, GPIO.HIGH)
time.sleep(3)
GPIO.output(relayPin, GPIO.LOW)
time.sleep(3)

while True:
    if GPIO.input(switchPin):
        GPIO.output(lightPin, GPIO.HIGH)
        GPIO.output(relayPin, GPIO.HIGH)
    else:
        GPIO.output(lightPin, GPIO.LOW)
        GPIO.output(relayPin, GPIO.LOW)


print("done!")
GPIO.cleanup
