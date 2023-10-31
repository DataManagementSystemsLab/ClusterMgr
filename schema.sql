-- CREATE USER 'owuser' IDENTIFIED BY 'pass4owCluster';
-- GRANT ALL PRIVILEGES ON owcluster.* TO 'owuser';


create database if not exists owcluster;
create table if not exists  owcluster.users (id int primary key AUTO_INCREMENT, username varchar(15) unique, lastname varchar(40), firstname varchar(40),
passwd varchar(40), hashpasswd varchar(40), secret_key char(40), grp varchar(20), email varchar(50) unique,  sent BOOLEAN , created BOOLEAN) ;
create table if not exists  owcluster.logs (id int primary key AUTO_INCREMENT ,username varchar(15), tm datetime, actn char(10));

Create table if not exists owcluster.vms (id int primary key AUTO_INCREMENT, indx int,
 ipaddr VARCHAR(15) unique, memory int, vcpu int,  vmtype varchar(10),
  macaddr varchar(30) unique,hostname varchar(30) unique, disk_image varchar(40),
   location varchar(10));

create table if not exists  owcluster.vmusers (id int primary key AUTO_INCREMENT, 
vmindx int, username varchar(15) unique ,passwd varchar(20), superuser boolean, sent boolean);



insert into vms(indx,hostname,vcpu,memory,ipaddr,macaddr,location) values (0,'khalefam',2,4,'10.100.04.00','ae:52:00:00:00:00', 'owhpc-00' );
insert into vms(indx,hostname,vcpu,memory,ipaddr,macaddr,location) values (1,'noutsosc',2,4, ,'10.100.04.01' ,'ae:52:00:00:00:01', 'owhpc-00');
insert into vms(indx,hostname, vcpu,memory,ipaddr,macaddr,location) values (2,'balyanr',2,4, '10.100.04.02','ae:52:00:00:00:02', 'owhpc-00' );
insert into vms(indx,hostname, vcpu, memory, ipaddr, macaddr, location ) values (3,'rayanas',2,4,'10.100.04.03','ae:52:00:00:00:03', 'owhpc-00');

insert into vms(indx,hostname,vcpu,memory,ipaddr,macaddr,location) values (10,'db',2,4,'10.100.4.55','ae:52:00:00:04:0a', 'owhpc-00' );
insert into vms(indx,hostname,vcpu,memory,ipaddr,macaddr,location) values (11,'net0',2,4,'10.100.4.56','ae:52:00:00:04:0b', 'owhpc-00' );
insert into vms(indx,hostname,vcpu,memory,ipaddr,macaddr,location) values (12,'net1',2,4,'10.100.4.57','ae:52:00:00:04:0c', 'owhpc-01' );


insert into vms(indx,hostname,vcpu,memory,ipaddr,macaddr,location) values (20,'pchau1',2,4, '10.100.6.50','ae:52:00:00:04:00', 'owhpc-00' );
insert into vms(indx,hostname,vcpu,memory,ipaddr,macaddr,location) values (21,'emastroc',2,4,'10.100.6.51','ae:52:00:00:04:01','owhpc-00' );
insert into vms(indx,hostname,vcpu,memory,ipaddr,macaddr,location) values (22,'vyashaev' ,2,4,'10.100.6.52','ae:52:00:00:04:02','owhpc-00');
insert into vms(indx,hostname, vcpu,memory,ipaddr,macaddr,location) values (23,'kthomp39',2,4,'10.100.6.53' ,'ae:52:00:00:04:03','owhpc-00');
# insert into vms(indx,hostname, vcpu,memory,ipaddr,macaddr,location) values (24,'jcozzoli',2,4,'10.100.6.54','ae:52:00:00:04:04', 'owhpc-00' );
#insert into vms(indx,hostname,vcpu,memory,ipaddr,macaddr,location) values (25,'cpeter16',2,4,'10.100.6.55','ae:52:00:00:04:05', 'owhpc-00' );

insert into vmusers(vmindx,username,passwd,superuser) values  (0,'khalefam','pass4owCluster',true);
insert into vmusers(vmindx,username,passwd,superuser) values  (1,'noutsosc','pass4owCluster',true);
insert into vmusers(vmindx,username,passwd,superuser) values  (2,'balyanr','pass4owCluster',true);
insert into vmusers(vmindx,username,passwd,superuser) values  (3,'rayanas','pass4owCluster',true);

insert into vmusers(vmindx,username,passwd,superuser) values  (10,'khalefam','pass4owCluster',true);
insert into vmusers(vmindx,username,passwd,superuser) values  (10,'jcozzoli','pass4owCluster',false);
insert into vmusers(vmindx,username,passwd,superuser) values  (10,'cpeter16','pass4owCluster',false);
insert into vmusers(vmindx,username,passwd,superuser) values  (10,'tverma','pass4owCluster',false);
insert into vmusers(vmindx,username,passwd,superuser) values  (10,'rshahid','pass4owCluster',false);

