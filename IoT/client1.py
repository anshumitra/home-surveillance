
import time
import sys
import pprint
import uuid
from uuid import getnode as get_mac

import RPi.GPIO as GPIO
import time

trig=16
echo=18
led=11
x=0 #led status
intruder=0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, 1) 

ls='OFF'

try:
	import ibmiotf.application
	import ibmiotf.device
except ImportError:
	# This part is only required to run the sample from within the samples
	# directory when the module itself is not installed.
	#
	# If you have the module installed, just use "import ibmiotf.application" & "import ibmiotf.device"
	import os
	import inspect
	cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"../../src")))
	if cmd_subfolder not in sys.path:
		sys.path.insert(0, cmd_subfolder)
	import ibmiotf.application
	import ibmiotf.device


def myAppEventCallback(event):
	print("Received live data from %s (%s) sent at %s: hello=%s x=%s" % (event.deviceId, event.deviceType, event.timestamp.strftime("%H:%M:%S"), data['hello'], data['x']))

def myCommandCallback(cmd):
  print("Command received: %s" % cmd.payload)
  if cmd.command == "on":
    print("Turning Light ON")
    x=1
    GPIO.output(led,1)

  elif cmd.command == "off":  
    print("Turning Light OFF")
    x=0
    GPIO.output(led,0) 

print       
#####################################
#FILL IN THESE DETAILS
#####################################     
organization = "s141xb"
deviceType = "raspberrypi"
deviceId = "b827ebf07633"
appId = str(uuid.uuid4())
authMethod = "token"
authToken = "GWN3Y8E)ITkRlEsZ0A"

# Initialize the device client.
try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
except Exception as e:
	print(str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()
deviceCli.commandCallback = myCommandCallback
#x=0
while(1):
	if x==0:
		ls='OFF'
	else:
		ls='ON'
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

        if distance<30:
            intruder = 1
        else:
            intruder = 0
	data = { 'LightStatus': ls, 'Intruder': intruder}
        deviceCli.publishEvent("status", data)
	#x=x+1
	time.sleep(1)
		

# Disconnect the device and application from the cloud
deviceCli.disconnect()
#appCli.disconnect()

