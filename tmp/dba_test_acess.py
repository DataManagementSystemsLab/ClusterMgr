import os
import db_access as dba

os.environ["DEBUSSY"] = "1"
os.environ['DB_HOST']="127.0.0.1"
os.environ['DB_USER']="radius"
os.environ['DB_PASS']="radpass"
c=dba.connect()
d=dict()
d["User-Name"]="mike" 
d["User-Password"]="mFQu_J[KXJ;LKBpl9"
d["Event-Timestamp"]= "Jan 07 2022 22:11:2 GMT"
 
dba.check_authorize(c, d)