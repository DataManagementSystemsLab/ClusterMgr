import utils
import sys
import users
import db_access as dba
import mysql.connector
import sync
import traceback
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
    'database': 'owcluster',}
    }
    argn=len(sys.argv)
    if argn==3 and sys.argv[1]=="import":
            try:
                source_db = mysql.connector.connect(**dbs['localdb'])
                users.import_account(source_db,sys.argv[2])
                source_db.close()
            except:
                traceback.print_exc()    
    if argn==2 and sys.argv[1]=="create":
            try:
                source_db = mysql.connector.connect(**dbs['localdb'])
                users.create_accounts(source_db)
                source_db.close()
            except:
                traceback.print_exc()    
    elif argn==2 and sys.argv[1]=="email":
            try:
                source_db = mysql.connector.connect(**dbs['localdb'])
                users.send_owaccount_emails(source_db)
                source_db.close()
            except:
                traceback.print_exc()    
    elif argn==2 and sys.argv[1]=="sync":
            try:
                source_db = mysql.connector.connect(**dbs['localdb'])
                destination_db = mysql.connector.connect(**dbs['remotedb'])
                sync.move_data(source_db,destination_db,"users","users")
                sync.move_data(source_db,destination_db,"users","users")
                sync.move_data(source_db,destination_db,"logs","logs")
                sync.move_data(source_db,destination_db,"vmusers","vmusers")
                sync.move_data(source_db,destination_db,"vms","vms")
                source_db.close()
                destination_db.close()
            except:
                traceback.print_exc()    
    elif argn==2 and sys.argv[1]=="rsync":
            try:
                source_db = mysql.connector.connect(**dbs['remotedb'])
                destination_db = mysql.connector.connect(**dbs['localdb'])
                sync.move_data(source_db,destination_db,"users","users")
                sync.move_data(source_db,destination_db,"logs","logs")
                sync.move_data(source_db,destination_db,"vmusers","vmusers")
                sync.move_data(source_db,destination_db,"vms","vms")
                source_db.close()
                destination_db.close()
            except:
                traceback.print_exc()    