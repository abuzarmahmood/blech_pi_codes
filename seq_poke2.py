# Import things for running pi codes
import time
from math import floor
import random
import RPi.GPIO as GPIO

from subprocess import Popen
import easygui
import numpy as np
import os

# Setup pi board
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
	
def seq_poke2(outputs = [31, 33, 35, 37], intaninputs = [24, 26, 19, 21], opentimes = [0.01, 0.01, 0.01, 0.01], iti = 14.0, trials = 240):
	
	light = 38 #assign port number to light
	poke = 13 #assign port number to nose poke

	GPIO.setmode(GPIO.BOARD) #start GPIO setup
	for i in outputs:
		GPIO.setup(i, GPIO.OUT) #loop through outputs to setup
	for i in intaninputs:
		GPIO.setup(i, GPIO.OUT) #loop through intaninputs to setup
	GPIO.setup(light, GPIO.OUT) #setup light output 
	GPIO.setup(poke, GPIO.IN) #setup poke input
		
	poke_latencies = [] #make array for storing poke latencies
	current_trial = 0 #establish start 
	
	assay_start = time.time() #establish start time

	i = 0 	# i counts the sequence
	
	for current_trial in range(trials): 
		
		GPIO.output(light, 1) # turn the light on
		sensor = 0 # the rat has not yet gone past the laser sensor
		
		start_time = time.time()# records when the current time when the trial starts
		# while loop during the time before 14 seconds is up
		while time.time() < start_time + iti:
			while time.time() < start_time + 1 and sensor == 0:
				GPIO.output(light, 0)
				time.sleep(0.1)
				GPIO.output(light, 1)
				time.sleep(0.1)
				if GPIO.input(poke) == 0 and sensor == 0:
					sensor = 1
					current_time = time.time() - start_time
					poke_latencies += [current_time]
					GPIO.output(light, 0)
					GPIO.output(outputs[i], 1)
					GPIO.output(intaninputs[i], 1)
					time.sleep(opentimes[i])
					GPIO.output(outputs[i], 0)
					GPIO.output(intaninputs[i], 0)

			if GPIO.input(poke) == 0 and sensor == 0:
				sensor = 1
				current_time = time.time() - start_time
				poke_latencies += [current_time]
				GPIO.output(light, 0)
				GPIO.output(outputs[i], 1)
				GPIO.output(intaninputs[i], 1)
				time.sleep(opentimes[i])
				GPIO.output(outputs[i], 0)
				GPIO.output(intaninputs[i], 0)
				
			
		if sensor == 0: 
			poke_latencies += [0]
			 	
		# iterate through the taste options whether the rat consumes or not
		i += 1
		# restart the taste sequence after all have been consumed or skipped
		if i == len(outputs):
			i = 0
				
		
		
	GPIO.output(light, 0)	
	a = raw_input("assay finished, would you like to save latency data? (y/n): ")
	if a == 'n':
		print("file not saved, exiting program")
		
	else:
		filename = raw_input("enter a filename, or enter 'cancel' to cancel: ")
		if filename == 'cancel':
			print("file not saved")
		else:
			np.save(filename, poke_latencies)
			print("file saved")
	
#seq_poke was written by Christina Mazzio and Daniel Svedberg, 2018			
		
	
			
			
			
			
			
			 
			
			
			
			
				
		
	
