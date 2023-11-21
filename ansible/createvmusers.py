import crypt 
import mysql.connector

# get users from the databases
source_db={
'owhpc' : {
    'host': '10.100.1.0',
    'user': 'owuser',
    'password': 'pass4owCluster',
    'database': 'owcluster',
    },
'local' :  {
    'host': '10.100.1.0',
    'user': 'owuser',
    'password': 'pass4owCluster',
    'database': 'owcluster',
    }
}
source_db = mysql.connector.connect(**source_db['local'])
source_cursor = source_db.cursor()
source_cursor.execute(f"select  ipaddr, username, superuser,passwd from vmusers u, vms v where u.vmindx=v.id';")

columns = [column[0] for column in source_cursor.description]
result_set = source_cursor.fetchall()


