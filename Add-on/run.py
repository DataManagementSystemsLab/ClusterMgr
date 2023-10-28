import utils
import sys
import users
import db_access as dba
import mysql.connector
import sync
#python3 run import file
#python3 run email file
#python3 run sync
if __name__ == "__main__":
    dbs={ 
    'localdb': {
    'host': '127.0.0.1',
    'user': 'owuser',
    'password': 'pass4owCluster',
    'database': 'owcluster',
    },
    'remotedb' : {
    'host': '151.181.203.21',
    'user': 'owuser',
    'password': 'pass4owCluster',
    'database': 'owcluster1',}
    }
    argn=len(sys.argv)
    if argn==3 and sys.argv[1]=="import":
            source_db = mysql.connector.connect(**dbs['localdb'])
            users.import_account(source_db,sys.argv[2])
            source_db.close()
    elif argn==3 and sys.argv[1]=="email":
            source_db = mysql.connector.connect(**dbs['localdb'])
            users.send_emails(source_db)
            source_db.close()
    elif argn==2 and sys.argv[1]=="sync":
            source_db = mysql.connector.connect(**dbs['localdb'])
            destination_db = mysql.connector.connect(**dbs['remotedb'])
            sync.move_data(source_db,destination_db,"users","users")
            source_db.close()
            destination_db.close()