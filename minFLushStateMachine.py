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
			if inp[0] == True:
				return ('flushing','startFlush')
			elif inp[0] == False:
				return ('waiting','waiting')
		elif state == 'flushing':
			if inp[1] == True:
				return ('flushing','flushing')
			elif inp[1] == False:
				return ('waiting','endFlush')


if __name__ == '__main__':
	sm = flushController()
	sm.start()

	while True:
		print 'readLight: ', readLight()
		print 'buttonState: ', buttonState()
		print sm.step()
		sleep(0.5)
