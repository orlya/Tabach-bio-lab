create schema organisms_proteins;

use organisms_proteins;

create table organisms_groups
(org_group_id varchar (64) primary key,
 org_group_name varchar(64));
 
 create table organisms_sub_groups
 (org_sub_group_id varchar(64) primary key,
  org_sub_group_name varchar(64));


create table organisms
(org_id varchar(4096) primary key,
 org_name varchar(1024), 
 org_group_id varchar(64),
 org_sub_group_id varchar(64),
 release_date date,
 modification_date date,
 org_source varchar(32),
 foreign key (org_group_id) references organisms_groups(org_group_id),
 foreign key (org_sub_group_id) references organisms_sub_groups(org_sub_group_id)
 );

 
 
 
 