from gpiozero import LightSensor

ldr1 = LightSensor(16)
while True:
    print ldr1.value
