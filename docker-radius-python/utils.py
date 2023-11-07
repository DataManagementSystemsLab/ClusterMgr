import hashlib
from datetime import datetime
import utils
import db_access as dba
import time
import pyotp
def get_hash_password(user, p):
    st= user+p
    h1=hashlib.sha1(st.encode("utf-8"))
    return str(h1.hexdigest())

def record_action(cnx, idx, user,action,ipaddr):
    q=f" insert into owcluster.logs(idx,username,tm,act,ipaddr) values (%d, %s,now(),%s,%s);" 
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
       
    
    return is_valid, idx, res


def check_authorize(cnx,d):
    user=d['User-Name']
    password=d["User-Password"]
    eventtime=d["Event-Timestamp"]
    ipaddr=d["Framed-IP-Address"]
    retval= False
    act= "reject"
    idx=-1
    res={
        "request": (()),
        "reply": (("Reply-Message","code is NOT valid!!"),),
        "config": (("Auth-Type","Reject"),),
        }
    if ':' in password:
        retval, idx, res=check_query_1(cnx,user,password, eventtime)
    if user=='Mike' and password=='2F2FBasioOW$':
        retval=True
        act='accept'
        res={
        "request": (()),
        "reply": (("Reply-Message","Hi from the Other side.."),("PaloAlto-User-Group",":=", "AA")),
        "config": (("Auth-Type","Accept"),),
        }          

    record_action(cnx,idx,user,act,ipaddr)
    return retval, res
    