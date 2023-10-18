create user 'sysadmin'@'localhost' Identified with mysql_native_password BY '1234';
grant all privileges on *.* to 'sysadmin'@'localhost';
flush privileges;