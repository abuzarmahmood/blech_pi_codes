# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 10:46:27 2018

@author: JYlabPC
"""


# Import things for running pi codes
import time
#from math import floor
#import random
import RPi.GPIO as GPIO

# Import other things for video
#from subprocess import Popen
#import easygui
#import numpy as np
#import os

# Setup pi board
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

# Basic nose poking procedure to train poking for discrimination 2-AFC task
def nose_poke_test(trials = 10):

    #intaninput = 8
    #trial = 1
    inport = 11
    pokelight = 36
    #houselight = 18
    #lights = 0
    #maxtime = 60

        # Setup pi board GPIO ports 
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pokelight, GPIO.OUT)
    GPIO.setup(inport, GPIO.IN)
    #GPIO.setup(outport, GPIO.OUT)
    #GPIO.setup(intaninput, GPIO.OUT)
	
    #time.sleep(15)
    #starttime = time.time()
    
    for i in range(trials):
        GPIO.output(pokelight, 1)        
        while GPIO.input(inport) == 1:
            time.sleep(0.1)
        GPIO.output(pokelight, 0) 
        print("trial" + str(i+1))
	time.sleep(5)
        
        
    
