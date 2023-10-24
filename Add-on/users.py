import utils
import sys
import db_access as dba
import pyotp
def send_emails(conn):
    results=conn.execute("SELECT id,username, email, passwd, firstname FROM owcluster.users where sent is NULL").fetchall()
    for row in  results:
        #print(row)
        id=row[0]
        username=row[1]
        user_email=row[2]
        password=row[3]
        firstname=row[4]
        
        utils.send_account_email(conn, username, password , user_email)
def send_vm_emails(conn):
    results=conn.execute("SELECT username, email, ipaddr FROM owcluster.vmusers where sent is NULL").fetchall()
    for row in  results:
        username=row[0]
        user_email=row[1]
        ipaddr=row[2]
 
        utils.send_vm_email(conn, username, ipaddr , user_email)
def create_accounts(conn):
  users=dba.run_query(conn,"select id, username from owcluster.users where created is Null;",None)
  for user in users:
    id=user[0]
    username=user[1]
    secret_key = pyotp.random_base32()
    password=utils.generate_password()
    hashedpassword=utils.get_hash_password(username, password)
    Q_user=f"update owcluster.users set passwd='{password}', hashpasswd='{hashedpassword}', secret_key='{secret_key}   where id='{id}');"
    conn.execute(Q_user) 
  conn.commit()   
