import crypt 
import mysql.connector
import runcmd as r
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
source_db = mysql.connector.connect(**source_db['owhpc'])
source_cursor = source_db.cursor()
source_cursor.execute(f"select  ipaddr, username, superuser,passwd from vmusers u, vms v where u.vmindx=v.indx and applied=False;")

columns = [column[0] for column in source_cursor.description]
result_set = source_cursor.fetchall()


for row in result_set:
    ipaddr = row[0]
    username = row[1]
    superuser = row[2]
    passwd = row[3]
    user=r.AddUser(username, passwd)
    commands=[]
    commands.append(f'userdel {username}')
    commands.append(str(user))
    if superuser == 1:
        commands.append(f'usermod -aG sudo {username}')
    
    
    r.run_command_remotely_asroot(ipaddr, 'sysadmin', 'linux', commands)