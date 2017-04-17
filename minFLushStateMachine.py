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

# output includes:
# flushing, waiting, flushDone
class flushController(sm.SM):
	startState = 'waiting'
	def getNextValues(self,state,inp):
		if state == 'waiting':
			changeLightState(0,'off')
			changeLightState(1,'off')
			if inp[0] == True:
				setValve('open')
				return ('flushing','startFlush')
			elif inp[0] == False:
				setValve('close')
				return ('waiting','waiting')
		elif state == 'flushing':
			changeLightState(0,'on')
			changeLightState(1,'on')
			if inp[1] == True:
				setValve('open')
				return ('flushing','flushing')
			elif inp[1] == False:
				setValve('close')
				return ('waiting','endFlush')


if __name__ == '__main__':
	sm = flushController()
	sm.start()

	while True:
		print 'readLight: ', readLight()
		print 'buttonState: ', buttonState()
		print sm.step()
		sleep(0.5)
