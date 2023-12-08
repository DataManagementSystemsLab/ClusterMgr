import utils
import sys
import db_access as dba
import pyotp
def send_owaccount_emails(conn):
    users=dba.run_query(conn,"SELECT id, username, email, passwd, firstname, secret_key FROM owcluster.users where email is not null and ((sent is NULL) or (sent=False));",None)
    for row in  users:
        #print(row)
      try:
        id=row[0]
        username=row[1]
        user_email=row[2]
        password=row[3]
        firstname=row[4]
        secret_key=row[5]
         
        utils.send_account_email(id, username, password ,firstname, user_email, secret_key)
        Q=f"UPDATE owcluster.users SET sent = True WHERE id = '{id}';"
        dba.run_query(conn,Q,None)
        
      except Exception as e:
        print (row)
        print(e)  
      conn.commit()


def send_vmusers_emails(conn):
    q='''select vu.id,u.firstname, vu.username, vu.passwd, v.ipaddr, u.email from owcluster.users u, owcluster.vmusers vu,
      owcluster.vms v  where u.id = vu.userid and vu.vmindx=v.indx and ((vu.sent is NULL) or (vu.sent=False));'''
    
    results=dba.run_query(conn,q,None)
    for row in  results:
        id=row[0]
        firstname=row[1]
        username=row[2]
        password=row[3]
        ipaddr=row[4]
        user_email=row[5]
        utils.send_vm_email(username, password, firstname,ipaddr , user_email)
        Q=f"UPDATE owcluster.vmusers SET sent = True WHERE id = '{id}';"
        dba.run_query(conn,Q,None)
    conn.commit()

def create_accounts(conn):
  users=dba.run_query(conn,"select id, username from owcluster.users where (created is Null) or (Created=False);",None)
  for user in users:
    id=user[0]
    username=user[1]
    print(id, username)
    secret_key = pyotp.random_base32()
    password=utils.generate_password()
    hashedpassword=utils.get_hash_password(username, password)
    Q_user=f"update owcluster.users set passwd='{password}', hashpasswd='{hashedpassword}', secret_key='{secret_key}', created=true where id='{id}';"
    print(Q_user)
    dba.run_query(conn,Q_user, None) 
  conn.commit()   

def import_account(conn, filename):
   # read a file line by line and split it into fields
   f = open(filename, 'r')
   for line in f:
     fields=line.split(',')
     lastname=fields[0]
     firstname=fields[1]
     username=fields[2]
     email=fields[3]
     #dba.run_query(conn,"select id, username from owcluster.users where username=%s;",(username,))
     Q_user=f"insert into owcluster.users (username, email, firstname, lastname) values ('{username}',  '{email}', '{firstname}', '{lastname}');"
     dba.run_query(conn,Q_user, None) 
   conn.commit()
