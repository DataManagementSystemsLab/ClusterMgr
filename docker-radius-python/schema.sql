-- CREATE USER 'radius'@'localhost' IDENTIFIED BY 'radpass';
-- GRANT ALL PRIVILEGES ON radius.* TO 'radius'@'localhost' WITH GRANT OPTION;


create database if not exists radius;
use radius;
create table if not exists  radius.users (id int primary key auto_increment, userid varchar(15),passwd varchar(40),
 secret_key char(40), grp varchar(20), email varchar(300), ts int(11) ) ;
create table if not exists  radius.logs (id int,userid varchar(15), tm datetime, actn char(10));



insert into radius.users(userid, passwd,secret_key, grp, email ) values ('mike','5f6fa2af41b6926d9e580b3ab176dd5e2d81317b','XIU6SQGYSCKQDKXVH4R5BW4TC7FXFNOJ', 'GP_Students', NULL);
insert into radius.users(userid, passwd,secret_key, grp, email ) values ('renu','c45dad0b75cd2d59ce157e8e7b547fe8d22d131d','XIU6SQGYSCKQDKXVH4R5BW4TC7FXFNOJ', 'GP_Students', 'khalefaow@gmail.com');



insert into radius.users(userid, passwd, secret_key, grp, email) values ('owcluster', '22ab520ac631c4acf9676840e79252888c1c2bee', '3UL74QIJ2F2RWGINSMHP4U3IOI2LQA3V', 'GP_Students', 'khalefaow@gmail.com');
insert into radius.users(userid, passwd, secret_key, grp, email) values ('owcluster', 'b01ebd2ae5690e61ab9b7da0c94f9d0a95985d76', 'Y5SAXCMQRRHWPD5A67OWPJP7YEB7K57B', 'GP_Students', 'khalefaow@gmail.com');
insert into radius.users(userid, passwd, secret_key, grp, email) values ('jcozzoli', 'cfe8616f4d7036961f7ff7698e28c939b2fa8e3f', '7INGLF3IASROAQPI35D2LXBIJDY7KRQF', 'GP_Students', 'jcozzoli@oldwestbury.edu');
insert into radius.users(userid, passwd, secret_key, grp, email) values ('kmertz1', '263a840ba5225c07836a83fd19241ad1bb2b9310', 'RFGW4WG6UJEEFFVKADBJZ3NGN4YFD7OQ', 'GP_Students', 'kmertz1@oldwestbury.edu');
insert into radius.users(userid, passwd, secret_key, grp, email) values ('cpeter16', 'b215b88522708107dd14c2ff37fc257b35814cf9', '5XLMU6TFWPN75LSJSOKJSH3W2R3JEFSD', 'GP_Students', 'cpeter16@oldwestbury.edu');
insert into radius.users(userid, passwd, secret_key, grp, email) values ('rshahid', 'd977f11c86242c3aab9fe916f058bfdf9318a8b6', '6GG7UX3EO2QVUOS4SESBASOZAUCCBSMG', 'GP_Students', 'rshahid@oldwestbury.edu');
insert into radius.users(userid, passwd, secret_key, grp, email) values ('tverma', '20f93c7a331143ec27439fdd417b4c80817c6709', 'CC3FZO7EVDPE7E6M7FTUOPWUMHO4U2E3', 'GP_Students', 'tverma@oldwestbury.edu');


insert into radius.users(userid, passwd, secret_key, grp, email) values ('pchau1', '6733193a5c4990454ac40c6dd602723fdca623d6', 'MA4XTG2HY5FFRJZGIG2QG2PXZANYXJK7', 'GP_Students', 'pchau1@oldwestbury.edu');
insert into radius.users(userid, passwd, secret_key, grp, email) values ('emastroc', '057d670447cc8a6b2fbdd92f295c04ce98ee7672', '6PEYK2D2B6QE6CDHYB2S7IZAWBJUZPS3', 'GP_Students', 'emastroc@oldwestbury.edu');
insert into radius.users(userid, passwd, secret_key, grp, email) values ('vyashaev', 'baa1f699d32e83ca108e8b5597b764f114c451d2', '56II5KYGBL227W5YTWZRZKE7VLODV3ZA', 'GP_Students', 'vyashaev@oldwestbury.edu');
insert into radius.users(userid, passwd, secret_key, grp, email) values ('kthomp39', '0f98bb736882701a41b6d3526b3db8d967a00b47', 'TFIFBB24MWZVT62ABMAVSU7SCMWKQ2R5', 'GP_Students', 'kthomp39@oldwestbury.edu');
insert into radius.users(userid, passwd, secret_key, grp, email) values ('noutsosc', '98dcf76bc245ad36972f1f811e62c72f5d4a9fb1', 'VLN26RL5OD3CLBLLQIHHU7BEWTLS2RG7', 'GP_Students', 'noutsosc@oldwestbury.edu');
insert into radius.users(userid, passwd, secret_key, grp, email) values ('jcozzoli', '8d06bc749ae0b205d1fe8519c482d7f1a49397b1', 'WVFGTUGF5BXUG5FEVH566UDNC3OMOOXU', 'GP_Students', 'jcozzoli@oldwestbury.edu');
insert into radius.users(userid, passwd, secret_key, grp, email) values ('cpeter16', 'e43bd8ca3d883ec677bbcd4d45248321efe0d158', 'V44ASOAJKRFW66FRIFXYUA5BJHXIHPP3', 'GP_Students', 'cpeter16@oldwestbury.edu');
