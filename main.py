#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from pybricks.parameters import Color, Port
from pybricks.iodevices import AnalogSensor, UARTDevice

# Write your program here
ev3 = EV3Brick()

motor1=Motor(Port.A)
motor2=Motor(Port.B)
spd = 180

del1= 1000 #delay for the track to move
del2= 1000 #delay for the spoon to swing down
del3= 2500

uart = UARTDevice(Port.S1, 9600, timeout=2000)

while(True):
    if uart.waiting() != 0:
        red = uart.read(1).decode("utf-8")
        if red == "1":
            motor2.run_time(spd,del2)#move spoon up 
            motor1.run_time(-spd,del1)#move brick off belt onto spoon
            motor2.run_time(spd,del3)#move spoon 270 degrees
        if red == "0":
            motor1.run_time(spd,del1)#move to next brick
        
        wait(1000)

