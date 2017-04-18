import RPi.GPIO as GPIO
import time
from time import time, sleep, ctime


GPIO.setmode(GPIO.BCM)
#import lightSensorInput
from lightSensorInput import readLight
print 'lightSensor Imported'
from FlushButtonInput import buttonState
print 'Button Initialised'
from valveControl import setValve
print 'valve Control online'
#import lightControl
#print 'lights activated'
from lightControl import changeLightState
print 'lights activated'
from minFLushStateMachine import flushController
print 'stateMachine a go'
import shitPresenceAlgo as sp
print 'AI alive'
from PushToFirebase import pushFlushDetail

###Setup will be done in the individual files.
# GPIO.setup(switchPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(lightPin, GPIO.OUT)
# GPIO.setup(relayPin, GPIO.OUT)

sm = flushController()
sm.start()

print 'Hello!'
changeLightState('on')
sleep(1)
changeLightState('off')
print 'there'

FlushDuration = 0
flushTime = 0
try:
	while True:
		output = sm.step([buttonState(),sp.shitPresent()])
		if output == 'waiting':
			print 'waiting'
		elif output == 'startFlush':
			flushTime = time()
			changeLightState('on')
			setValve('open')
			print "startedFlush"
		elif output == 'flushing':
			print 'flushing'
		elif output == 'endFlush':
			flushDuration = time()-flushTime
			changeLightState('off')
			print 'time lag'
			sleep(1.5)
			setValve('close')
			flushTime = ctime(flushTime)
			print 'flushStartTime: ', flushTime
			print 'flushing took: ', flushDuration
			pushFlushDetail(flushTime,round(flushDuration,1))
		sleep(0.5)
except KeyboardInterrupt:
	setValve('close')
	changeLightState('off')
	GPIO.cleanup()













