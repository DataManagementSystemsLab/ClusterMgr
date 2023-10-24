

def import_users(filename):
 with open(filename) as f:
                first_line=True
                for line in f:
                    if first_line:
                        first_line=False
                        continue
                    fields=line.strip().split(',')
                    if len(fields) != 4:
                        continue
                    (conn,fields[2],fields[3]) 


if __name__ == "__main__":
    
    n=len(sys.argv)
    if n>1:
        
        if n==2:
            #read a csv file as argument and create users
            #open file and iterate over lines
            with open(sys.argv[1]) as f:
                first_line=True
                for line in f:
                    if first_line:
                        first_line=False
                        continue
                    fields=line.strip().split(',')
                    if len(fields) != 4:
                        continue
                    utils.create_account(conn,fields[2],fields[3]) 
        else:
            for argc in sys.argv[1:]:
                print(argc)
                utils.create_account(conn, argc,'khalefaow@gmail.com')
    #init_db(conn)
    #utils.create_account(conn,'A1', 'khalefaow@gmail.com');
    else:
        send_emails(conn)
        send_vm_emails(conn)
    conn.close()