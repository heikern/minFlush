from libdw import sm
from time import time, sleep


import lightSensorInput
from lightSensorInput import readLight
from FlushButtonInput import buttonState

# inp includes
# 0: the state of button press
# 1: the value of the light sensor
class flushController(sm.SM):
	startState = 'waiting'
	def getNextValues(self,state,inp):
		if state == 'waiting':
			if inp[0] == True:
				return ('flushing','Imma Flushing')
			elif inp[0] == False:
				return ('waiting','Imma waiting')
		elif state == 'flushing':
			if inp[1] < 390:
				return ('flushing','I will still flush')
			elif inp[1] >= 390:
				return ('waiting','I am done flushing')



sm = flushController()
sm.start()

while True:
	print 'readLight: ', readLight()
	print 'buttonState: ', buttonState()
	print sm.step([buttonState(),readLight()])
	sleep(0.5)
