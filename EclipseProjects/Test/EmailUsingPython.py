#!/usr/bing/python3

import smtplib
from http.client import HTTPSConnection

httpsConn = ''
msg = ''

try:
    
    print("Starting connection")
          
    httpsConn = smtplib.SMTP('smtp.mail.com', 587)
    
    print("Connection established")
    httpsConn.ehlo()
    httpsConn.starttls()
    httpsConn.ehlo()
    httpsConn.login('test39909@mail.com', 'justtest39909')
    
    from1 = 'test39909@mail.com'
    to = 'test39909@mail.com'
    
    message = 'This is a test e-mail message.'
       
    msg = "\r\n".join([
          "From: test39909@mail.com",
          "To: test39909@mail.com",
          "Subject: Test email",
          "",
          "Test email"
          ])
    
    print('Message ready to send')
    
    httpsConn.sendmail(from1, to, msg)
    
    print("Message sent, attempting to close connection")
    httpsConn.close()
    print("Message sent, closed connection")
    
    print('Email successfully sent')

except:
    print("Problem with connection")  
    
    