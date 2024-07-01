-- Create table USERS
-- depends: 20240627_01_qqogo-create-database-yoyotest
create table users (id serial primary key, name varchar(50), email varchar(50) unique);
