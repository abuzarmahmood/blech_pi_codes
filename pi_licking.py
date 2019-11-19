# Import things for running pi codes
import time
import sys
import Adafruit_MPR121.MPR121 as MPR121
from math import floor
import random
import RPi.GPIO as GPIO

# Import other things for video
from subprocess import Popen
import easygui
import numpy as np
import os

# Setup pi board
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)



# Create MPR121 instance.
cap = MPR121.MPR121()

# Initialize communication with MPR121 using default I2C bus of device, and
# default I2C address (0x5A).  On BeagleBone Black will default to I2C bus 0.
if not cap.begin():
    print('Error initializing MPR121.  Check your wiring!')
    sys.exit(1)

# Main loop to print a message every time a pin is touched.
#print('Press Ctrl-C to quit.')


def pi_licking(intaninputs = [7]):


        # Setup pi board GPIO ports
	GPIO.setmode(GPIO.BOARD)
	for i in intaninputs:
		GPIO.setup(i, GPIO.OUT)
	GPIO.output(intaninputs[0], 0)	
	last_touched = 0

        while True: 
            current_touched = cap.touched()
        # Check each pin's last and current state to see if it was pressed or released.
            for i in range(12): # change this since only one is used
            # Each pin is represented by a bit in the touched value.  A value of 1
            # means the pin is being touched, and 0 means it is not being touched.
                pin_bit = 1 << i
            # First check if transitioned from not touched to touched.
                if current_touched & pin_bit and not last_touched & pin_bit:
                	GPIO.output(intaninputs[0], 1) 
                	print('{0} touched!'.format(i))
            # Next check if transitioned from touched to not touched.
                if not current_touched & pin_bit and last_touched & pin_bit:
                	GPIO.output(intaninputs[0], 0)
			print('{0} released!'.format(i))
        # Update last state and wait a short period before repeating.
            last_touched = current_touched




