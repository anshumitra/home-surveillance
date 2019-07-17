import time
import RPi.GPIO as GPIO

led2=11 #pin 11

GPIO.setmode(GPIO.BOARD)
#GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
#GPIO.output(led1,GPIO.LOW)
GPIO.output(led2,GPIO.HIGH)

while True:
	#GPIO.output(led1, GPIO.HIGH)
	GPIO.output(led2, GPIO.LOW)
	time.sleep(0.5)
	#GPIO.output(led1, GPIO.LOW)
	GPIO.output(led2, GPIO.HIGH)
	time.sleep(0.5)
GPIO.cleanup()
