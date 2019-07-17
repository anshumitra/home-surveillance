#from time import sleep,time()
import time
import RPi.GPIO as GPIO
from picamera import PiCamera

camera= PiCamera()


GPIO.setmode(GPIO.BOARD)

trig=16 #pin 16
echo=18 #pin 18 

x=0

while True:
	print "Measuring distance"

	GPIO.setup(trig,GPIO.OUT)
	GPIO.setup(echo,GPIO.IN)

	GPIO.output(trig,False)
	time.sleep(2)

	GPIO.output(trig,True)
	time.sleep(0.00001)
	GPIO.output(trig,False)

	while GPIO.input(echo)==0:
		pulse_start=time.time()
	
	while GPIO.input(echo)==1:
		pulse_final=time.time()
	
	pulse_duration=pulse_final-pulse_start

	distance = pulse_duration*17150

	distance= round(distance,2)

	print "Distance ",distance," cm"
	
	if distance < 30:
		camera.start_preview()
		camera.exposure_mode='antishake'
		time.sleep(1)
		camera.capture('/home/pi/Desktop/Python/image%s.jpg' %x)
		x=x+1
		camera.stop_preview()

GPIO.cleanup()
