
```sql
create user 'sysadmin'@'localhost' Identified with mysql_native_password BY '1234';
grant all privileges on *.* to 'sysadmin'@'localhost';
flush privileges;

```
```
ssh add key

```



create user 'sysadmin'@'localhost' Identified with mysql_native_password BY '1234';
grant all privileges on *.* to 'sysadmin'@'localhost';
flush privileges;

 ips   = [for i in range(var.hosts) : "10.100.5.${format("%s", i + 50)}"]
  names = ["khalefam","pchau1", "emastroc", "vyashaev", "kthomp39", "noutsosc", "jcozzoli", "cpeter16", "balyanr"]
  macs  = [for i in range(var.hosts) : "ae:52:0a:b0:05:${format("%02x", i + 50)}"]
  memory = ["4048", "4048", "4048", "4048", "4048", "4048", "4048","4048", "4048"]	 

}