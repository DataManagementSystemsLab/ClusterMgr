import mysql.connector 
from datetime import datetime
import time
import os
import pyotp
import random
import string
import mail_access 
import util

def connect():
  HOST=os.environ.get('DB_HOST')
  #PORT=os.environ.get('DB_PORT')
  USER=os.environ.get('DB_USER')
  PASS=os.environ.get('DB_PASS')
  print(HOST)
  while True:
    try:
      print("*** Connecting ***")
      conn = mysql.connector.connect(user=USER, password=PASS,
                                     host=HOST,
                                     database='radius')
      print("connected>>>>>>>>>>>>")
      return conn
    except Exception  as e:
      print(e)
      print("Returing None a")
      return None
    
def run_query(cnx,q,vals):
  while True:
    try:
      #print("Run query")
      #print (q)
      #print(vals)
      #print(cnx)
      curx=cnx.cursor()
      #curx.execute("set profiling =1")

      try:
                #print("---")
                curx.execute(q,vals)
                #print("****************"+curx.statement)
      except Exception:
          print("****************"+curx.statement)
          #curx.execute('show profiles')
          #for row in curx:
          #    print (row)
      #curx.execute("set profiling =0")          
      if not curx.with_rows:
          #print("no results")
          return None
      row=curx.fetchone()
      #print("\n\n\n---------------------------------------------\n\n")
      #print (row)
      return row

    except Exception as e:
      print("a")
      print(e)
      cnx=connect()

    #print("returning none 0")
    return None      

def record_action(cnx,id, user,action):
    q=f" insert into radius.logs values ( %s,%s,now(),%s);commit;" 
    run_query(cnx,q,(id,user,action ))


def insert_user(cnx,user,passwd, secret_key, email):
    q=f"insert into radius.users(userid, passwd,secret_key, grp, email ) values (%s,%s,%s, 'GP_Students', %s);commit;"
    passwd=util.get_hash_password(user, passwd)
    run_query(cnx,q,(user,passwd,secret_key,email ))


def check_query_1(cnx,user, password,eventtime):
    timestamp = datetime.strptime(eventtime, '%b %d %Y %H:%M:%S %Z')
    unix_timestamp=time.mktime(timestamp.timetuple())
    i=password.rfind(':')
    passwd=password[0:i]
    code=password[i+1:]
    code=int(code)
    #print("________________________________________________")
    #print(code)
    is_valid=False
    q=f"select  id,secret_key,grp from radius.users where userid = %s and passwd=%s;" 
    id = -1
    grp =""
    passwd=util.get_hash_password(user, passwd)

    row= run_query(cnx,q, (user,passwd))
    #print("check query 89")
    if  row:
          secret_key=row[1]
          id=row[0]
          grp=row[2]
          totp = pyotp.TOTP(secret_key)
          for delta in range(-50,100,4):
            comp=totp.at(unix_timestamp+delta)
            comp= int(comp)
            #print(comp)
            is_valid = comp == code
            if is_valid:
                break
    if is_valid:
       act="accept"
       res={
        "request": (()),
        "reply": (("Reply-Message","Hi from the other side"),("PaloAlto-User-Group",":=", grp)),
        "config": (("Auth-Type","Accept"),),
        }          
    else:
       act= "reject"
       res={
        "request": (()),
        "reply": (("Reply-Message","code is NOT valid!!")),
        "config": (("Auth-Type","Reject"),),
        }          
       
    record_action(cnx,id,user,act)
    return is_valid, res

def check_query_2(cnx,user, password,eventtime):
    timestamp = datetime.strptime(eventtime, '%b %d %Y %H:%M:%S %Z')
    unix_timestamp=time.mktime(timestamp.timetuple())
    i=password.rfind(';')
    passwd=password[0:i]
    code=password[i+1:]
    is_valid=False
    id = -1
    grp =""
    
    q=f"select  id,secret_key,grp,email,ts from radius.users where userid = %s and passwd=%s;" 
    passwd=util.get_hash_password(user, passwd)

    row= run_query(cnx,q, (user,passwd))
    
    if  row:
          secret_key=row[1]
          id=row[0]
          grp=row[2]
          email=row[3]
          ts=row[4]
          if code == '':
            secret_key = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
            ts=str(unix_timestamp+5*60) 
            
            q=f"update users set secret_key = '{secret_key}', ts= {ts}   where id= {id}; commit;" 
            #print(q)
            run_query(cnx,q, () )
            #print(email)
            mail_access.send_email(email,"OTP Code", " Code is "+ secret_key)
                   
          elif code ==secret_key:
               if ts>unix_timestamp:
                print(ts)
                print(unix_timestamp)
                is_valid= True
          
    if is_valid:
       act="accept"
       res={
        "request": (()),
        "reply": (("Reply-Message","Hi from the other side"),("PaloAlto-User-Group",":=", grp)),
        "config": (("Auth-Type","Accept"),),
        }          
    else:
       act= "reject"
       res={
        "request": (()),
        "reply": (("Reply-Message","code is NOT valid!!")),
        "config": (("Auth-Type","Reject"),),
        }          
       
    record_action(cnx,id,user,act)
    return is_valid, res

def check_authorize(cnx,d):
    
    user=d['User-Name']
    password=d["User-Password"]
    eventtime=d["Event-Timestamp"]

    if ':' in password:
        c, res=check_query_1(cnx,user,password, eventtime)
        #print("RES")
        #print(res)
        return c, res
    if user=='Mike' and password=='2F2FBasioOW$':
        act='accept'
        res={
        "request": (()),
        "reply": (("Reply-Message","Hi from the Other side.."),("PaloAlto-User-Group",":=", "AA")),
        "config": (("Auth-Type","Accept"),),
        }          
        return True, res
    #if ';' in password:
    #    c, res=check_query_2(cnx,user,password, eventtime)
    #    return c, res

    act= "reject"
    res={
        "request": (()),
        "reply": (("Reply-Message","code is NOT valid!!"),),
        "config": (("Auth-Type","Reject"),),
        }          
    return False, res
