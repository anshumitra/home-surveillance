import time
import RPi.GPIO as GPIO

led1=22
led2=11

GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.cleanup()