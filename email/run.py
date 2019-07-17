import sys
import ast
from datetime import datetime
 
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

import time
import RPi.GPIO as GPIO
from picamera import PiCamera


camera= PiCamera()


GPIO.setmode(GPIO.BOARD)

trig=16 #pin 16
echo=18 #pin 18 
 
print "Measuring distance"

	GPIO.setup(trig,GPIO.OUT)
	GPIO.setup(echo,GPIO.IN)

	GPIO.output(trig,False)
	time.sleep(0.1)

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
		camera.capture('/home/pi/Desktop/email/image.jpg')
		x=x+1
		camera.stop_preview()

time.sleep(1)
 
class Bimail:
	def __init__(self,subject,recipients):
		self.subject = subject
		self.recipients = recipients
		self.htmlbody = ''
		self.sender = "barbxsingh@gmail.com"
		self.senderpass = 'mymail23account'
		self.attachments = []
 
	def send(self):
		msg = MIMEMultipart('alternative')
		msg['From']=self.sender
		msg['Subject']=self.subject
		msg['To'] = ", ".join(self.recipients) # to must be array of the form ['mailsender135@gmail.com']
		msg.preamble = "preamble goes here"
		#check if there are attachments if yes, add them
		if self.attachments:
			self.attach(msg)
		#add html body after attachments
		msg.attach(MIMEText(self.htmlbody, 'html'))
		#send
		s = smtplib.SMTP('smtp.gmail.com:587')
		s.starttls()
		s.login(self.sender,self.senderpass)
		s.sendmail(self.sender, self.recipients, msg.as_string())
		#test
		# print msg
		s.quit()
	
	def htmladd(self, html):
		self.htmlbody = self.htmlbody+'<p></p>'+html
 
	def attach(self,msg):
		for f in self.attachments:
		
			ctype, encoding = mimetypes.guess_type(f)
			if ctype is None or encoding is not None:
				ctype = "application/octet-stream"
				
			maintype, subtype = ctype.split("/", 1)
 
 
			if maintype == "text":
				fp = open(f)
				# Note: we should handle calculating the charset
				attachment = MIMEText(fp.read(), _subtype=subtype)
				fp.close()
			elif maintype == "image":
				fp = open(f, "rb")
				attachment = MIMEImage(fp.read(), _subtype=subtype)
				fp.close()
			elif maintype == "audio":
				fp = open(f, "rb")
				attachment = MIMEAudio(fp.read(), _subtype=subtype)
				fp.close()
			else:
				fp = open(f, "rb")
				attachment = MIMEBase(maintype, subtype)
				attachment.set_payload(fp.read())
				fp.close()
				encoders.encode_base64(attachment)
			attachment.add_header("Content-Disposition", "attachment", filename=f)
			attachment.add_header('Content-ID', '<{}>'.format(f))
			msg.attach(attachment)
	
	def addattach(self, files):
		self.attachments = self.attachments + files
 
 
 
#example below
if __name__ == '__main__':	
	# subject and recipients
	mymail = Bimail('Sales email ' +datetime.now().strftime('%Y/%m/%d'), ['anshuman.joy@gmail.com'])
	#start html body. Here we add a greeting. 
	mymail.htmladd('Good morning, find the daily summary below.')
	#Further things added to body are separated by a paragraph, so you do not need to worry about newlines for new sentences
	#here we add a line of text and an html table previously stored in the variable
	mymail.htmladd('Daily sales')
	##mymail.htmladd(htmlsalestable)
	#another table name + table
	mymail.htmladd('Daily bestsellers')
	##mymail.htmladd(htmlbestsellertable)
	# add image chart title
	mymail.htmladd('Weekly sales chart')
	#attach image chart
	mymail.addattach(['image.jpg'])
	#refer to image chart in html
	#mymail.htmladd('<img src="image.jpg"/>') 
	#attach another file
	mymail.addattach(['bimail.py'])
	#send!
	mymail.send()


