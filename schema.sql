-- CREATE USER 'owuser' IDENTIFIED BY 'pass4owCluster';
-- GRANT ALL PRIVILEGES ON owcluster.* TO 'owuser';


create database if not exists owcluster;
create table if not exists  owcluster.users (id int primary key AUTO_INCREMENT, username varchar(15) unique, lastname varchar(40), firstname varchar(40),
passwd varchar(40), hashpasswd varchar(40), secret_key char(40), grp varchar(20), email varchar(50) unique,  sent BOOLEAN , created BOOLEAN) ;
create table if not exists  owcluster.logs (id int primary key AUTO_INCREMENT ,idx int, username varchar(15), tm datetime, actn char(10), 
ipaddr varchar(15));

Create table if not exists owcluster.vms (id int primary key AUTO_INCREMENT, indx int,
 ipaddr VARCHAR(15) unique, memory int, vcpu int,  vmtype varchar(10),
  macaddr varchar(30) unique,hostname varchar(30) unique, disk_image varchar(40),
   location varchar(10), managed boolean default false, notes varchar(100));

create table if not exists  owcluster.vmusers (id int primary key AUTO_INCREMENT, 
vmindx int, username varchar(15)  ,passwd varchar(20), superuser boolean, sent boolean,
unique (vmindx, username), userid int);


