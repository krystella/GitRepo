# -*- coding: utf-8 -*-
"""
Project: Email Sender
@author: Krystella Rattan
"""

from email.message import EmailMessage
from password import gmail_password

        ## Note: 'password' is file in which the unique app password issued by the email provider is stored to reduce the risk of sharing with unauthorised persons. Alternatively, the app password can be stored directly to the variable email_password


## To create context
import ssl
import smtplib

email_sender = # input sender email here
email_password = gmail_password # input unique app password here

email_receiver = # insert receiver email address here

subject = 'Test email'
body = """
This is a test email. It was coded to you in Python.
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    