import time
import RPi.GPIO as GPIO

led = 22
pir = 11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(pir,GPIO.IN, GPIO.PUD_DOWN)
#GPIO.output(led,GPIO.HIGH)

while True:
	pir_out=GPIO.input(pir)
        if pir_out == 0:
            print "No intruders ", pir_out
            GPIO.output(led,GPIO.LOW)
            time.sleep(0.1)
        elif pir_out == 1:
            print "Intruders", pir_out
            GPIO.output(led,GPIO.HIGH)
            time.sleep(0.1)

GPIO.cleanup()
