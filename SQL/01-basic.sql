create database deg;

use deg;

create table Associate(
    a_id int primary key,
    a_name varchar(255) not null,
    a_des varchar(255),
    a_addr varchar(255)
);

select * from Associate;

INSERT INTO Associate(a_id, a_name, a_des, a_addr) VALUES
(1, 'mahesh', 'Manager', 'Pathardi phata'),
(2, 'saurabh', 'TL', 'Jail road'),
(3, 'shahu', 'Supervisor', 'Pimpalad'),
(4, 'rahul', 'Employee', 'vilholi'),
(5, 'amol', 'Assistant manager', 'Dubai'),
(6, 'Pratham', 'TL', 'Germany'),
(7, 'Gaurabv', 'Manager', 'Mumbai'),
(8, 'rahul', 'Employee', 'Pune'),
(9, 'suyog', 'Assistant manager', 'Thane'),
(10, 'tushar', 'Supervisor', 'Dhule');


select a_name from Associate;

select * from Associate;

select distinct a_des from Associate;

select a_name from Associate limit 5;

select * from Associate order by a_name;




