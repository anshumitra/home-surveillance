

# barbxsingh@gmail.com / mymail23account
# https://www.google.com/settings/security/lesssecureapps

import sys
import ast
from datetime import datetime
import smtplib

gmail_user = "barbxsingh@gmail.com"
gmail_pwd = "mymail23account"
TO = 'anshuman.joy@gmail.com'
SUBJECT = "Testing sending using gmail"
TEXT = "Testing sending mail using gmail servers"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_user, gmail_pwd)
BODY = '\r\n'.join(['To: %s' % TO,
        'From: %s' % gmail_user,
        'Subject: %s' % SUBJECT,
        '', TEXT])

server.sendmail(gmail_user, [TO], BODY)
print ('email sent')

