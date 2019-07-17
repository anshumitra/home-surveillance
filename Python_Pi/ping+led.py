
import time
import RPi.GPIO as GPIO

trig=16 #pin 16
echo=18 #pin 18 
led=11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, GPIO.HIGH)

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
		GPIO.output(led,1)
	else:
		GPIO.output(led,0)

GPIO.cleanup()
