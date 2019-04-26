create database Dictoray;
create table user( id int primary key auto_increment,
     name varchar(32) not null,
     passwd varchar(16) default "000000");


create table hist(
     id int primary key auto_increment,
     name varchar(32) not null,
     word varchar(32) not null,
     time varchar(64));


create table words(
     id int primary key auto_increment,
     word varchar(32),
     mean text,
     index(word));
