-- CREATE USER 'owuser' IDENTIFIED BY 'pass4owCluster';
-- GRANT ALL PRIVILEGES ON owcluster.* TO 'owuser';


create database if not exists owcluster;
create table if not exists  owcluster.users (id int primary key AUTO_INCREMENT, username varchar(15) unique, lastname varchar(40), firstname varchar(40),
passwd varchar(40), hashpasswd varchar(40), secret_key char(40), grp varchar(20), email varchar(50) unique,  sent BOOLEAN , created BOOLEAN) ;
create table if not exists  owcluster.logs (id int primary key AUTO_INCREMENT ,username varchar(15), tm datetime, actn char(10));

Create table if not exists owcluster.vms (id int primary key AUTO_INCREMENT, 
ipaddr VARCHAR(15) unique, memory int, vcpu int,  macaddr varchar(30),hostname varchar(30), disk_image varchar(40));

create table if not exists  owcluster.vmusers (id int primary key AUTO_INCREMENT,  username varchar(15) unique ,passwd varchar(20), superuser boolean, sent boolean);


