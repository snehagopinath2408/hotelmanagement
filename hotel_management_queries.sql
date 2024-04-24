create database hotel;
use hotel;


create table custdata(custname varchar(20),addr varchar (30),indate varchar(10),outdate
varchar(10));
 

 
create table roomtype (sno int primary key,roomtype varchar(10),rent int);
insert into roomtype values ('1','type A',1000);
insert into roomtype values ('2','type B',2000);
insert into roomtype values ('3','type C',3000);
insert into roomtype values ('4','type D',4000);
 

create table restaurant (sno int primary key ,itemname varchar(10),rate float);
insert into restaurant values(1,"tea",10);
insert into restaurant values(2,"coffee",10);
insert into restaurant values(3,"colddrink",20);
insert into restaurant values(4,"samosa",10);
insert into restaurant values(5,"sandwich",50);
insert into restaurant values(6,"Dhokla",30);
insert into restaurant values(7,"kachori",10);
insert into restaurant values(8,"milk",20);
insert into restaurant values(9,"noodles",50);
insert into restaurant values(10,"pasta",50);

create table laundry(sno int primary key,itemname varchar(10),rate float);
insert into laundry values(1,"pant",10);
insert into laundry values(2,"shirt",10);
insert into laundry values(3,"suit",10);
insert into laundry values(4,"sari",10);

select* from custdata;
drop table custdata;