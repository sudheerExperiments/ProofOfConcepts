#!/usr/bing/python3

import smtplib
from http.client import HTTPSConnection

httpsConn = ''
msg = ''

try:
    
    print("Starting connection")
          
    httpsConn = smtplib.SMTP("test39909@mail.com:587")
    
    print("1")
    httpsConn.ehlo()
    httpsConn.starttls()
    httpsConn.ehlo()
    httpsConn.login('test39909@mail.com', 'justtest39909')
    
    from1 = 'test39909@mail.com'
    to = 'test39909@mail.com'
       
    msg = "\r\n".join([
          "From: test39909@mail.com",
          "To: test39909@mail.com",
          "Subject: Test email",
          "",
          "Test email"
          ])
    
    print('Message ready to send')
    
    httpsConn.send(from1, to, msg)
    httpsConn.close()
    
    print('Sending email successful')

except:
    print("Problem with connection")  
    
    