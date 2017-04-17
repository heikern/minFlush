import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time
from time import time

import lightSensorInput
from lightSensorInput import readLight
from FlushButtonInput import buttonState
from valveControl import setValve
from lightControl import changeLightState
from minFlushStateMachine import flushController
import shitPresenceAlgo as sp


# pin definition
# input pin
switchPin = 21
#output pin
lightPin = 26
# note. relay pin is active low
relayPin = 22
# light control pin
lightControl = 5

###Setup will be done in the individual files.
# GPIO.setup(switchPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(lightPin, GPIO.OUT)
# GPIO.setup(relayPin, GPIO.OUT)

sm = flushController()
sm.start()

startFlushTime = 0
flushTime = 0
while True:
	output = sm.step([buttonState(),sp.shitPresent()])
	if output == 'waiting':
		print 'waiting'
	elif output == 'startFlush':
		startFlushTime = time()
		changeLightState('on')
		setValve('open')
		print "startedFlush"
	elif output == 'flushing':
		print 'flushing'
	elif output == 'endFlush':
		flushTime = time()-startFlushTime
		changeLightState('off')
		setValve('close')
		print 'flushing took: ', flushTime
	time.sleep(0.2)














