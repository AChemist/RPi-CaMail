# Code to sense motion using an passive infra red (PIR) sensor on a Raspberry PI.
# After detection of motion a photo is recorded using the PiCamera and send via Mail.

# Resources
# 

# Librarys
import time 
import RPi.GPIO as GPIO
import smptlib

# Settings
import mailSettings

# Functions


# 
GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)



def MOTION(PIR_PIN):
	print "Motion Detected!"

print "PIR Module Test (CTRL+C to exit)"
time.sleep(2)
print "Ready"

try:
	GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
	while 1:
		time.sleep(100)

except KeyboardInterrupt:
	print  " -> Quit"
	GPIO.cleanup()
