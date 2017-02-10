#!/usr/bin/python

from gpiozero import LightSensor
import Tkinter as tkinter
from Tkinter import Canvas
window = tkinter.Tk()

#global Variable
hover = False

# sensorBinding
ldr1 = LightSensor(16)


# event handler
def readSensor(event):
    hover = True
    print ldr1.value
    if hover == True:
        window.after(10, readSensor(event))
def stopReading(event):
    hover = False
    print 'Stop'

# formating the window
window.title('Sensor Array')
window.geometry("300x300")
# Code to add widgets will go here...
TitleLabel = tkinter.Label(window,text="Sensor Grid")
w = Canvas(window, width=200, height=100)
w.create_rectangle(50, 25, 150, 75, fill="blue")
b = tkinter.Button(None, text='Mouse Clicks')
b.bind('<Enter>',readSensor)
b.bind('<Leave>',stopReading)

TitleLabel.grid(row=0,columnspan=2)
w.grid(row=1)
b.grid(row=3)

window.mainloop()
