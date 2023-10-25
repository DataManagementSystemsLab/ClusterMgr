import mysql.connector 
import os

def connect_base(host, user, password):
  while True:
    try:
      print("*** Connecting ***")
      conn = mysql.connector.connect(user=user, password=password,
                                     host=host,
                                     database='owcluster')
      print("connected>>>>>>>>>>>>")
      return conn
    except Exception  as e:
      print(e)
      print("Returing None a")
      return None

def connect():
  host='127.0.0.1'
  user='root'
  password='1234'
  return connect_base(host,user,password)

def connect_():
   HOST=os.environ.get('DB_HOST')
   USER=os.environ.get('DB_USER')
   PASS=os.environ.get('DB_PASS')
   return connect_base(HOST,USER,PASS)


def run_query(cnx,q,vals):
    try:
      curx=cnx.cursor()
      try:
        if vals is None:
          curx.execute(q)
        else:  
          curx.execute(q,vals)
      except Exception:
          print("****************"+curx.statement)
      if not curx.with_rows:
          return None
      rows=curx.fetchall()
      return rows
    except Exception as e:
      print(e)
    return None      
