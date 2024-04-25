import smtplib, ssl
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.application import MIMEApplication
import pyotp
import time
import json

import qrcode
#import matplotlib.pyplot as plt
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
    special_symbols = '!#$%&()*+,-./<=>?@{|}~'  # Remove underscore and hyphen
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
        box_size=12,
        border=2,
    )
    qr.add_data(qrcode_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="white", back_color="green")
    img.save("qrcode_"+username+".png")

def generate_json_file(username,   passwd ,secret_key):
    data = {
        "user": username,
        "password":passwd,
        "secret": secret_key
    }
    with open("credentials.json", "w") as write_file:
        json.dump(data, write_file)

def send_account_email( userid, username, passwd ,firstname, user_email, secret_key):
    msg = MIMEMultipart()
    body = f'''
    Hi {firstname},<br/>
    <br/>
    To access the OW cluster, follow the following steps: 
      <ol>
    <li>   Download Global Protect from https://151.181.203.6 <br/>
           [you need to click on Advanced, click on proceed to 151.181.203.6]
    </li>
    <li>  While connecting it may ask you for installing the certificate, as we have created account with the attached self-signed cert . 
    <ol>	For <b>windows</b>:
     <li>  Install the certificate as a local account.  </li>
    <li>  a location -> Browse and select Trusted root CA folder. </li>
    <li>    Once completed these steps, try reconnecting to GP and it should work. </li>
    </ol>
    <ol>	For <b>mac</b>:
    <li>  Install the certificate as a local account. follow steps from <a href="https://support.apple.com/guide/keychain-access/add-certificates-to-a-keychain-kyca2431/mac"> apple</a>   </li>
    <li>  find the certificate, and select always trust.   </li>
    <li>    Once completed these steps, try reconnecting to GP and it should work. </li>
     </ol>
    <br/>
    '''
    body += f'''
    <b>userid</b>: <u>{userid}</u><br/>
  <b>username</b>:<u>{username}</u><br/>
  <b>password</b>: '<u>{passwd}</u>' followed by ':' then the code from authenticator app from the attached image. <br/>
  '''
   
    msg['Subject'] = "Credentials for OWCluster Account!"
    msg['From'] = sender_email
    msg['To'] = user_email
    
    msg.attach(MIMEText(body, 'html'))
    gen_qrcode(username,secret_key)
    filename = "qrcode_"+username+".png"
    attachment = open(filename, "rb")
    imgp = MIMEBase('application', 'octet-stream')
    imgp.set_payload((attachment).read())
    encoders.encode_base64(imgp)
    imgp.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(imgp)

    attachment_path = "owcertificate.zip"  # Replace with the path to your ZIP file
    with open(attachment_path, "rb") as attachment:
        part = MIMEApplication(attachment.read(), Name="owcertificate.zip")
        part['Content-Disposition'] = f'attachment; filename="{part.get_filename()}"'
    msg.attach(part)

    ##add file
    generate_json_file(username, passwd, secret_key)
    attachment_path = "credentials.json"  # Replace with the path to your ZIP file
    with open(attachment_path, "rb") as attachment:
        part = MIMEApplication(attachment.read(), Name="credentials.json")
        part['Content-Disposition'] = f'attachment; filename="{part.get_filename()}"'
    msg.attach(part)




    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, gmailpassword)
        server.send_message(msg, from_addr=sender_email, to_addrs=user_email)
    

def send_vm_email(username, password, firstname, ipaddr,user_email):
    msg = MIMEMultipart()
    body = f'''
    Hi {firstname},<br/>
    <br/>
    To access the VM use the following credentials: <br/>
        IP:  {ipaddr}<br/>
       Username:  {username}<br/>
       Password: {password} <br/>
    '''
    msg['Subject'] = "Credentials for VM"
    msg['From'] = sender_email
    msg['To'] = user_email

    msg.attach(MIMEText(body, 'html'))
    
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, gmailpassword)
        server.send_message(msg, from_addr=sender_email, to_addrs=user_email)
    
