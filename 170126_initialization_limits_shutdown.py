#!/usr/bin/python

#170126_initialization_limits_shutdown.py

import wx
import ArcusDeviceModified as ADM
import time

### simple script that initializes the stepper motors, one at a time
### then, performs + and - limit routines, one at a time
### then, turns off the motors, one at a time
### the idea is to develop a set of wake up and go to sleep procedures

# initialize the y-axis motor

arc = ADM.ArcusDevice() #ADM.ArcusDevice is a class object that give you a
						#method to write to the stepper motor controller
						#as well as a method to close the connection to 
						#the controller

yMoto = ADM.ArcusStepperChannel(arc,
								axis = 'Y',
								min = 0,
								max = 100000,
								acceleration = 1000,
								lca = 8000,
								hspd = 4000,
								lspd = 400) #ADM.ArcusStepperChannel is a 
											#class object that has many methods
											#for controlling the stepper motors

yMoto.TurnMotorOn() #uses the 'EO' command to check if the motor is enabled or not
					#if it is already on, a message stating so is printed
					#if it is not, the 'EO=1' command is sent to the controller
					#to enable the motor

yMoto.GoToLimit(polarity = '+') #moves the motor in the + direction until the limit swith is hit
								#then, moves in the - direction by the distance
								#specified by the 'lca' argument in the stepper
								#channel definition

print('+ limit completed')
time.sleep(5)
print('starting - limit procedure in 1 second')
time.sleep(1)

yMoto.GoToLimit(polarity = '-')

print('- limit completed')
time.sleep(5)
print('starting move to relative position of 0.5 in 1 second')
time.sleep(1)

yMoto.SetAbsolutePosition(pos=0.5, wait=1) #move to a position that is half
										   #way between the motors min and 
										   #max values
										   #note that if wait is '0', the 
										   #function will finish before the
										   #move is made. 

print('relative move to 0.5 complete')
print('turning y motor off now')

yMoto.TurnMotorOff()

### now try the x axis
xMoto = ADM.ArcusStepperChannel(arc,
								axis = 'X',
								min = 0,
								max = 100000,
								acceleration = 1000,
								lca = 8000,
								hspd = 4000,
								lspd = 400) #ADM.ArcusStepperChannel is a 
											#class object that has many methods
											#for controlling the stepper motors

xMoto.TurnMotorOn() #uses the 'EO' command to check if the motor is enabled or not
					#if it is already on, a message stating so is printed
					#if it is not, the 'EO=1' command is sent to the controller
					#to enable the motor

xMoto.GoToLimit(polarity = '+') #moves the motor in the + direction until the limit swith is hit
								#then, moves in the - direction by the distance
								#specified by the 'lca' argument in the stepper
								#channel definition
								#SOMETHING DEFINITELY WRONG WITH THE + LIMIT
								#SWITCH ON THE XAXIS. THE STAGE HITS THE SWITCH
								#BUT THE MOTOR KEEPS ATTEMPTING TO TURN.

print('+ limit completed')
time.sleep(5)
print('starting - limit procedure in 1 second')
time.sleep(1)

xMoto.GoToLimit(polarity = '-')

print('- limit completed')
time.sleep(5)
print('starting move to relative position of 0.5 in 1 second')
time.sleep(1)

xMoto.SetAbsolutePosition(pos=0.5, wait=1) #move to a position that is half
										   #way between the motors min and 
										   #max values
										   #note that if wait is '0', the 
										   #function will finish before the
										   #move is made. 

print('relative move to 0.5 complete')
print('turning x motor off now')

xMoto.TurnMotorOff()




arc.Close()