import pyotp
import qrcode
import sys
import os
import db_access as dba
import hashlib
import random
import mail_access
import time

def get_passwd(input_string,l=12):
  # Convert string to UTF-8
  utf8_bytes = input_string.encode('utf-8')

  # Hash the UTF-8 bytes using SHA-256
  hash_object = hashlib.sha256(utf8_bytes)
  hash_bytes = hash_object.digest()

  # Define the character set for encoding
  character_set = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@;#$%&*_+=!?^~<>()[]{}\'"'

  # Generate the encoded hash by looking up characters in the character set
  random_generator = random.Random(10)
  hash_bytes = bytearray(hash_bytes)
  random_generator.shuffle(hash_bytes)
  encoded_hash = ''.join(character_set[b % len(character_set)]
                         for b in hash_bytes)

  return encoded_hash[:l]

def create_user(user,email):
        secret_key = pyotp.random_base32()
        print(secret_key)

        totp = pyotp.TOTP(secret_key)
        qrcode_data = totp.provisioning_uri(name=user, issuer_name='OW HPC Cluster')
        qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
                )
        qr.add_data(qrcode_data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="green", back_color="white")
        img.save("qrcode.png")

        #save
        #os.environ["DEBUSSY"] = "1"
        #os.environ['DB_HOST']="127.0.0.1"
        #os.environ['DB_USER']="radius"
        #os.environ['DB_PASS']="radpass"
        c=dba.connect()
        ts=time.time()
        passwd=get_passwd("Password1"+user+":"+email+":"+str(ts))
        dba.insert_user(c,user,passwd, secret_key, email)
        print(passwd)
        body="user:"+user +"\n"+"passwd:"+passwd +"\n"
        mail_access.send_email_with_attachment(email, "OW Cluster", body, "qrcode.png")


if len(sys.argv) > 1:
        user=sys.argv[1]
        email=sys.argv[2]
        create_user(user,email)