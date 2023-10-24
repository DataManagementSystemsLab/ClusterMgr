import smtplib, ssl
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import pyotp
import time

import pyotp

import qrcode
import matplotlib.pyplot as plt
import random
import string
import hashlib
import db_access as dba

from PIL import Image 
import PIL 

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "owcluster@gmail.com"  # Enter your address
gmailpassword = "cbqqqjuoekydaqey"

def get_hash_password(user, p):
    st= user+p
    h1=hashlib.sha1(st.encode("utf-8"))
    return str(h1.hexdigest())

def generate_password(length=8):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_symbols = string.punctuation.replace('_', '').replace('-', '').replace(':','').replace(';','')  # Remove underscore and hyphen
    all_characters = uppercase_letters + lowercase_letters + digits + special_symbols
    password = random.choice(uppercase_letters + lowercase_letters)
    for _ in range(length - 1):  # Subtract 1 to account for the first letter
        password += random.choice(all_characters)

    return password

def gen_qrcode(username, secret_key):
    totp = pyotp.TOTP(secret_key)
    qrcode_data = totp.provisioning_uri(name=username, issuer_name='OW HPC')
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=4,
    )
    qr.add_data(qrcode_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="green", back_color="white")
    img.save("/tmp/qrcode_"+username+".png")



def send_account_email(conn, username, password , user_email):
    msg = MIMEMultipart()
    body = "Account Information for OWCluster\n\n" 
    body= body + """ To access the cluster:
     Download Global Protect from https://151.181.203.6 provide your GP creds. [you need to click on Advanced, click on proceed to 151.181.203.6]

    While connecting it will ask you for installing the certificate, as we have created account with self-signed cert. 
    Install it as a local account 
    And then it will ask you for a location -> Browse and select Trusted root CA folder.
    Once completed these steps, try reconnecting to GP and it should work.

    Gateway is 151.181.203.6


    The password to use is one the format of 
        accesscode (provided below) followed by ':' then  the code from authenticator app.
    
    """

    body += "Username: "+username+"\n\n"
    
    body += "AccessCode: "+password+"\n\n"
    
    
    
    msg['Subject'] = "Credentials for OWCluster Account!"
    msg['From'] = sender_email
    msg['To'] = user_email
    
    msg.attach(MIMEText(body, 'plain'))
    
    filename = "qrcodes/qrcode_"+username+".png"
    attachment = open(filename, "rb")
    imgp = MIMEBase('application', 'octet-stream')
    imgp.set_payload((attachment).read())
    encoders.encode_base64(imgp)
    imgp.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(imgp)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, gmailpassword)
        server.send_message(msg, from_addr=sender_email, to_addrs=user_email)
    print(username)
    Q=f"UPDATE users SET sent = True, passwd= NULL WHERE username = '{username}';"
    conn.execute(Q)
    conn.commit()
    
def send_vm_email(conn, username, ipaddr , user_email):
    msg = MIMEMultipart()
    body = "Account Information VM\n\n" 
    body += "IP: "+ipaddr+"\n\n"
    body += "Username: "+username+"\n\n"
    body += "Password: "+"owclusterpass1"+"\n\n"
    
    msg['Subject'] = "Credentials for VM"
    msg['From'] = sender_email
    msg['To'] = user_email
    
    msg.attach(MIMEText(body, 'plain'))
    
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, gmailpassword)
        server.send_message(msg, from_addr=sender_email, to_addrs=user_email)
    print(username)
    Q=f"UPDATE vms SET sent = True WHERE username = '{username}';"
    conn.execute(Q)
    conn.commit()
