#!/usr/bin/python
import RPi.GPIO as GPIO
import time

LedPin = 11   # pin11

GPIO.setmode(GPIO.BOARD)        # Numbers GPIOs by physical location
GPIO.setup(LedPin, GPIO.OUT)    # Set LedPin's mode as output
GPIO.output(LedPin, GPIO.HIGH)  # Set LedPin as high(+3.3V) to turn off the led


try:
    while True:
        print '...led on'
        GPIO.output(LedPin, GPIO.LOW)   # led on
        time.sleep(0.5)
        print 'led off...'
        GPIO.output(LedPin, GPIO.HIGH)  # led off
        time.sleep(0.5)
except KeyboardInterrupt:               # CTRL-C
    GPIO.output(LedPin, GPIO.HIGH)      # led off
    GPIO.cleanup()                      # release resource
