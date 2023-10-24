import mysql.connector 
import os


def connect():
  HOST=os.environ.get('DB_HOST')
  USER=os.environ.get('DB_USER')
  PASS=os.environ.get('DB_PASS')
  
  while True:
    try:
      print("*** Connecting ***")
      conn = mysql.connector.connect(user=USER, password=PASS,
                                     host=HOST,
                                     database='owcluster')
      print("connected>>>>>>>>>>>>")
      return conn
    except Exception  as e:
      print(e)
      print("Returing None a")
      return None
    
def run_query(cnx,q,vals):
  while True:
    try:
      curx=cnx.cursor()
      try:
                #print("---")
                curx.execute(q,vals)
                #print("****************"+curx.statement)
      except Exception:
          print("****************"+curx.statement)
      if not curx.with_rows:
          return None
      rows=curx.fetchall()
      return rows
    except Exception as e:
      print("a")
      print(e)
      cnx=connect()
    return None      
