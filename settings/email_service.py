'''
#The purpose of this file to specify the htlm format in which the email is to be sent
'''
from __future__ import print_function
import smtplib

import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(email_ids, text):
    '''
    Here we are sending email to user
    '''
    sender = 'eway.bill@in.pwc.com'
    sendername = 'PwC Einvoice Solution'
    recipient = email_ids.split(",")
    username_smtp = "AKIAIXL6BNFTQVD3YKIQ"
    password_smtp = "AnXt5pZxsbFopf4Rm1eUr1bB0U2zc6V3nxRHW+ouelO4"
    host = "email-smtp.us-east-1.amazonaws.com"
    port = 587
    subject = 'Data Failure Notification'
    body_text = (text)
    msg = MIMEMultipart('alternative')
    #Subject for the email
    msg['Subject'] = subject
    #Sender of the email
    msg['From'] = email.utils.formataddr((sendername, sender))
    #Receivers of the email
    msg['To'] = email_ids
    part1 = MIMEText(body_text, 'html')
    msg.attach(part1)
    try:
        server = smtplib.SMTP(host, port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        #Logging in the email with user name and password
        server.login(username_smtp, password_smtp)
        #Sending the email
        server.sendmail(sender, recipient, msg.as_string())
        server.close()
    except Exception as error:
        print("L1: EXCEPTION OCCURED ", str(error))
