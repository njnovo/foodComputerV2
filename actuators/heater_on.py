import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(6, GPIO.OUT)

GPIO.output(6, GPIO.LOW)

time.sleep(6)
