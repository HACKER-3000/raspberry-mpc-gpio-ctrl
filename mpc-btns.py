#!/usr/bin/env python2

import RPi.GPIO as GPIO
import time

SHUTDOWN = 0
NEXT = 0
PP = 0
PREV = 0
VOLDOWN = 0
VOLUP = 0


GPIO.setmode(GPIO.BCM)
GPIO.setup(SHUTDOWN, GPIO.IN)
GPIO.setup(NEXT, GPIO.IN)
GPIO.setup(PREV, GPIO.IN)
GPIO.setup(VOLUP, GPIO.IN)
GPIO.setup(VOLDOWN, GPIO.IN)
GPIO.setup(PP, GPIO.IN)

while True:
	if GPIO.input(SHUTDOWN) == 1:
			os.system ("sudo shutdown now")
			
	if GPIO.input(PP) == 1:
			os.system ("mpc toggle")
			
	if GPIO.input(NEXT) == 1:
			os.system ("mpc next")
			
	if GPIO.input(PREV) == 1:
			os.system ("mpc prev")
			
	if GPIO.input(VOLDOWN) == 1:
			os.system ("mpc volume -10")
			
	if GPIO.input(VOLUP) == 1:
			os.system ("mpc volume +5")

