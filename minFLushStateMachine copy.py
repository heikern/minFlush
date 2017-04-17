from libdw import sm
from time import time, sleep


import lightSensorInput
from lightSensorInput import readLight
from FlushButtonInput import buttonState
from valveControl import setValve
from lightControl import changeLightState

# inp includes
# 0: the state of button press
# 1: the output of shitPresence Model

# output includes
class flushController(sm.SM):
	startState = 'waiting'
	def getNextValues(self,state,inp):
		if state == 'waiting':
			changeLightState(0,'off')
			changeLightState(1,'off')
			if inp[0] == True:
				setValve('open')
				return ('flushing','Imma Flushing')
			elif inp[0] == False:
				setValve('close')
				return ('waiting','Imma waiting')
		elif state == 'flushing':
			changeLightState(0,'on')
			changeLightState(1,'on')
			if inp[1] == True:
				setValve('open')
				return ('flushing','I will still flush')
			elif inp[1] == False:
				setValve('close')
				return ('waiting','I am done flushing')


if __name__ == '__main__':
	sm = flushController()
	sm.start()

	while True:
		print 'readLight: ', readLight()
		print 'buttonState: ', buttonState()
		print sm.step([buttonState(),readLight(7)])
		sleep(0.5)
