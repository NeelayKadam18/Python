import os
from sys import *

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def SendEmail(email):
    sender = 'aditi.pujari91@gmail.com'
    receivers = [email]

    port = 1025
    msg = MIMEText('This is test mail')

    msg['Subject'] = 'Birthday Wish'
    msg['From'] = sender
    msg['To'] = email

    with smtplib.SMTP('localhost', port) as server:
        # server.login('username', 'password')
        server.sendmail(sender, receivers, msg.as_string())
        print("Successfully sent email")

def main():
    print("Directory Watcher Application")

    #if(len(argv) < 2):
    #    print("Insufficient Arguments")
    #    exit()

    #if(argv[1] == "-h"):
    #    print("This script will traverse the directory and display the name of all the entries.")
    #    exit()

    #if(argv[1] == "-u"):
    #    print("Usage : Application_name Directory_name")
    #    exit()

    SendEmail("janhavigunjal@gmail.com")

if __name__ == "__main__":
    main()