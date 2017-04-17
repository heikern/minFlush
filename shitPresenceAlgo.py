from lightSensorInput import readLight

lightSensThreshold = {
	0: 250,
	1: 250,
        2: 250,
        3: 250,
        4: 250,
        5: 250
}

def shitPresent():
        sum = 0
        for i in range(0,6):
               if readLight(i)<lightSensThreshold[i]:
                       sum += 1
        print readLight(0), readLight(1), readLight(2),readLight(3),readLight(4),readLight(5)
	if sum == 6:
		return False
	else:
		return True
