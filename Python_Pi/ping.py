# comments
# connections
#  pin2 = +ve
#  pin6 = -ve
#
# ultrasound:
#   vcc = +ve
#   gnd = -ve
#   trig = pin16
#   echo = pin18 (with volt divider)
#       trig-1k-pin18-2k-gnd
#       because: rasp-pi supplies 5v,
#         but accepts 3.3v on data port


import time
import RPi.GPIO as GPIO

GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)

trig=16 #pin 16
echo=18 #pin 18 

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

GPIO.cleanup()
