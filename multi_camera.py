'''
pi_rig contrains basic functions for using the raspberry pi behavior and electrophysiology rig in the Katz Lab

These functions can be used directly via ipython in a terminal window or called by other codes
'''

# Import things for running pi codes
import time
from math import floor
import random

# Import other things for video
from subprocess import Popen
import easygui
import numpy as np
import os

process = Popen('streamer -q -c /dev/video1 -s 1280x720 -f jpeg -t 180 -r 30 -j 75 -w 0 -o video0.avi', shell = True, stdout = None, stdin = None, stderr = None, close_fds = True)

process = Popen('streamer -q -c /dev/video1 -s 1280x720 -f jpeg -t 180 -r 30 -j 75 -w 0 -o video1.avi', shell = True, stdout = None, stdin = None, stderr = None, close_fds = True)

process = Popen('streamer -q -c /dev/video2 -s 1280x720 -f jpeg -t 180 -r 30 -j 75 -w 0 -o video2.avi', shell = True, stdout = None, stdin = None, stderr = None, close_fds = True)
