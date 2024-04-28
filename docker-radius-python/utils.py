import hashlib
from datetime import datetime
import utils
import db_access as dba
import time
import pyotp

def record_action(cnx, idx, user,action,ipaddr):
    q=f" insert into owcluster.logs(idx,username,tm,actn,ipaddr) values (%s, %s,now(),%s,%s);" 
    #dba.run_query(cnx,q,(id,user,action ))
    curx=cnx.cursor()
    curx.execute(q,(idx, user,action,ipaddr ))
    cnx.commit()


#def insert_user(cnx,user,passwd, secret_key, email):
#    q=f"insert into owcluster.users(username, passwd,secret_key, grp, email ) values (%s,%s,%s, 'GP_Students', %s);commit;"
#    passwd=util.get_hash_password(user, passwd)
#    run_query(cnx,q,(user,passwd,secret_key,email ))

def check_query_1(cnx,user, password,eventtime):
    timestamp = datetime.strptime(eventtime, '%b %d %Y %H:%M:%S %Z')
    unix_timestamp=time.mktime(timestamp.timetuple())
    i=password.rfind(':')
    passwd=password[0:i]
    code=password[i+1:]
    code=int(code)
    is_valid=False
    q=f"select id,secret_key,grp from owcluster.users where username = %s and hashpasswd=%s;" 
    idx = -1
    grp =""
    passwd=utils.get_hash_password(user, passwd)
    curx=cnx.cursor()
    curx.execute(q,(user,passwd))
    rows=curx.fetchall()
    if len(rows)>0:
          row=rows[0]
          print(row)
          idx=row[0]
          secret_key=row[1]
          grp=row[2]
          totp = pyotp.TOTP(secret_key)
          prev_comp=-1
          for delta in range(-50,100,4):
            comp=totp.at(unix_timestamp+delta)
            comp= int(comp)
            if comp==prev_comp:
                continue
            prev_comp=comp
            print(comp)
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
       
    
    return is_valid, idx,act, res

def xor_bytes(byte_array1, byte_array2):
    result = bytes(b1 ^ b2 for b1, b2 in zip(byte_array1, byte_array2))
    return result
def check_user(row, timestart,userdigest):
    idx=row[0]
    secret_key=row[1]
    grp=row[2]
    hpasswd=bytes.fromhex(row[3])
    totp = pyotp.HOTP(secret_key)
    counter=int(timestart/30)
    
    for delta in range(-5,5,1):
        user_code=totp.at(counter+delta)
        #print("counter"+str(counter+delta))
        #print("user"+str(user_code))
        generated_code = hashlib.sha1(user_code.encode()).digest()
        #print(generated_code.hex())
        gendigest = xor_bytes(hpasswd, generated_code)
        #print(gendigest.hex())
        #print(userdigest)
        is_valid = gendigest.hex()==userdigest
        #print(is_valid)
        if is_valid:
                return 1, idx
    return 0, idx

def check_query_2(cnx,user, userdigest,eventtime):
    print(userdigest)
    timestamp = datetime.strptime(eventtime, '%b %d %Y %H:%M:%S %Z')
    unix_timestamp=time.mktime(timestamp.timetuple())
    is_valid=False
    q=f"select id,secret_key,grp,hashpasswd from owcluster.users where username = %s;" 
    idx = -1
    grp =""
    
    curx=cnx.cursor()
    curx.execute(q,(user,))
    rows=curx.fetchall()
    if len(rows)>0:
        for row in rows:
              print(row)
              is_valid, idx=check_user(row, unix_timestamp,userdigest)
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
       
    
    return is_valid, idx,act, res

def check_authorize(cnx,d):
    print(d)
    user=d['User-Name']
    password=d["User-Password"]
    eventtime=d["Event-Timestamp"]  if "Event-Timestamp" in d else ""
    ipaddr=d["Framed-IP-Address"] if "Framed-IP-Address" in d else ""
    retval= False
    act= "reject"
    idx=-1
    res={
        "request": (()),
        "reply": (("Reply-Message","code is NOT valid!!"),),
        "config": (("Auth-Type","Reject"),),
        }
    
    
    if ':' in password:
        retval, idx,act, res=check_query_1(cnx,user,password, eventtime)
    elif len(password)==40:
        retval, idx,act, res=check_query_2(cnx,user,password, eventtime)
    record_action(cnx,idx,user,act,ipaddr)
    return retval, res
    
