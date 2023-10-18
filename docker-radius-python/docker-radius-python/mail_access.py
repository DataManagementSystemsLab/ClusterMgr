import smtplib, ssl
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import json

def send_email(receiver_email, Subject, Body):    
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "owcluster@gmail.com"  # Enter your address
    receiver_email = receiver_email # Enter receiver address
    with open('secret.json') as file:
        data = json.load(file)
    password = data["password"]

    msg = EmailMessage()
    msg.set_content(Body)
    msg['Subject'] = Subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.send_message(msg, from_addr=sender_email, to_addrs=receiver_email)


def send_email_with_attachment(receiver_email, Subject, Body, filename):    
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "owcluster@gmail.com"  # Enter your address
    with open('secret.json') as file:
        data = json.load(file)

    password = data["password"]
    msg = MIMEMultipart()
    body = Body

    msg['Subject'] = Subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
  
    msg.attach(MIMEText(body, 'plain'))
    attachment = open(filename, "rb")
    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')
    # To change the payload into encoded form
    p.set_payload((attachment).read())
    # encode into base64
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.send_message(msg, from_addr=sender_email, to_addrs=receiver_email)
    

