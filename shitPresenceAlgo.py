from lightSensorInput import readLight

lightSensThreshold = {
	0: 400,
	1: 400
}

def shitPresent():
	if lightSensThreshold[0]-readLight(0) < 0:
		return True
	else:
		return False
