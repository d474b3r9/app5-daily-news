import smtplib
import ssl
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(message):
    host = "smtp.gmail.com"
    port = 465  # TLS
    smtp_user = os.getenv('SMPT_USERS')
    smtp_key = os.getenv('SMTP_KEY')

    receiver = smtp_user
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(smtp_user, smtp_key)
        server.sendmail(smtp_user, receiver, message)


smtp_server = "smtp.gmail.com"
port = 587  # For starttls
smtp_user = os.getenv('SMPT_USERS')
smtp_key = os.getenv('SMPT_KEY')

# Create a secure SSL context
context = ssl.create_default_context()

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendmailx(message):
    message = MIMEMultipart()
    message["To"] = smtp_user
    message["From"] = smtp_user
    message["Subject"] = 'Subject line here.'

    title = '<b> Title line here. </b>'
    message_text = MIMEText('''Message body goes here.''', 'html')
    message.attach(message_text)

    email = smtp_user
    password = smtp_key

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo('Gmail')
    server.starttls()
    server.login(email, password)
    fromaddr = 'From line here.'
    toaddrs = 'Address you send to.'
    server.sendmail(fromaddr, toaddrs, message.as_string())

    server.quit()
