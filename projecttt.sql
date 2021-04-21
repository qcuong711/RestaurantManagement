create database projecttt;
use projecttt;

ALTER TABLE employee AUTO_INCREMENT = 1;

select * from manager;
select * from employee;
select * from drinks;
select * from foods; 

create table manager (
	m_id varchar(20) not null primary key,
    m_name varchar(50) not null,
    salary float not null
);

create table employee (
	e_id varchar(20) not null primary key,
    e_name varchar(50) not null,
    m_id varchar(20) not null,
    hire_date date not null,
    job varchar(20) not null,
    salary float not null,
    foreign key(m_id) references manager(m_id)
);

create table drinks (
	d_id varchar(20) not null primary key,
    d_name varchar(20) not null,
    d_price float not null
);

create table foods (
	f_id varchar(20) not null primary key,
    f_name varchar(20) not null,
    f_price float not null
);

-- Danh sach quan li
insert into manager(m_id, m_name, salary)
values ('M1', 'VAN THANH', '17000000');

insert into manager(m_id, m_name, salary)
values ('M2', 'HUY HUNG', '22500000');

insert into manager(m_id, m_name, salary)
values ('M3', 'TIEN LINH', '21800000');

-- Danh sach nhan vien
insert into employee(e_id, e_name, m_id, hire_date, job, salary)
values ('E1', 'VAN LAM', 'M1', Str_To_Date('17-11-2017', '%d-%m-%Y'), 'BAO VE', '6500000');

insert into employee(e_id, e_name, m_id, hire_date, job, salary)
values ('E2', 'NGUYEN MANH', 'M1', Str_To_Date('05-03-2018', '%d-%m-%Y'), 'BAO VE', '5800000');

insert into employee(e_id, e_name, m_id, hire_date, job, salary)
values ('E3', 'VAN DUC', 'M2', Str_To_Date('09-06-2018', '%d-%m-%Y'), 'DAU BEP', '11000000');

insert into employee(e_id, e_name, m_id, hire_date, job, salary)
values ('E4', 'CONG PHUONG', 'M2', Str_To_Date('05-07-2018', '%d-%m-%Y'), 'DAU BEP', '12500000');

insert into employee(e_id, e_name, m_id, hire_date, job, salary)
values ('E5', 'HUNG DUNG', 'M2', Str_To_Date('01-09-2018', '%d-%m-%Y'), 'DAU BEP', '12700000');

insert into employee(e_id, e_name, m_id, hire_date, job, salary)
values ('E6', 'TUAN ANH', 'M2', Str_To_Date('04-08-2018', '%d-%m-%Y'), 'NHAN VIEN PHA CHE', '9000000');

insert into employee(e_id, e_name, m_id, hire_date, job, salary)
values ('E7', 'DUC CHINH', 'M2', Str_To_Date('19-03-2018', '%d-%m-%Y'), 'NHAN VIEN VE SINH', '5600000');

insert into employee(e_id, e_name, m_id, hire_date, job, salary)
values ('E8', 'TIEN DUNG', 'M2', Str_To_Date('07-08-2018', '%d-%m-%Y'), 'NHAN VIEN VE SINH', '5400000');

insert into employee(e_id, e_name, m_id, hire_date, job, salary)
values ('E9', 'XUAN TRUONG', 'M3', Str_To_Date('11-07-2018', '%d-%m-%Y'), 'BOI BAN', '5900000');

insert into employee(e_id, e_name, m_id, hire_date, job, salary)
values ('E10', 'DUC HUY', 'M3', Str_To_Date('22-04-2018', '%d-%m-%Y'), 'BOI BAN', '6500000');

insert into employee(e_id, e_name, m_id, hire_date, job, salary)
values ('E11', 'DUY MANH', 'M3', Str_To_Date('25-03-2019', '%d-%m-%Y'), 'BOI BAN', '5600000');

insert into employee(e_id, e_name, m_id, hire_date, job, salary)
values ('E12', 'ANH DUC', 'M3', Str_To_Date('12-05-2019', '%d-%m-%Y'), 'BOI BAN', '5400000');

insert into employee(e_id, e_name, m_id, hire_date, job, salary)
values ('E13', 'DINH TRONG', 'M3', Str_To_Date('30-01-2019', '%d-%m-%Y'), 'BOI BAN', '5200000');

insert into employee(e_id, e_name, m_id, hire_date, job, salary)
values ('E14', 'HONG DUY', 'M3', Str_To_Date('23-12-2018', '%d-%m-%Y'), 'BOI BAN', '5750000');

insert into employee(e_id, e_name, m_id, hire_date, job, salary)
values ('E15', 'QUANG HAI', 'M3', Str_To_Date('11-01-2018', '%d-%m-%Y'), 'BOI BAN', '5900000');

insert into employee(e_id, e_name, m_id, hire_date, job, salary)
values ('E16', 'TRONG HOANG', 'M3', Str_To_Date('02-03-2019', '%d-%m-%Y'), 'BOI BAN', '5000000');

insert into employee(e_id, e_name, m_id, hire_date, job, salary)
values ('E17', 'MINH VUONG', 'M3', Str_To_Date('07-04-2018', '%d-%m-%Y'), 'BOI BAN', '5300000');

insert into employee(e_id, e_name, m_id, hire_date, job, salary)
values ('E18', 'TUAN MANH', 'M3', Str_To_Date('04-02-2018', '%d-%m-%Y'), 'BOI BAN', '5400000');

insert into employee(e_id, e_name, m_id, hire_date, job, salary)
values ('E19', 'XUAN MANH', 'M3', Str_To_Date('07-05-2018', '%d-%m-%Y'), 'BOI BAN', '5800000');

-- Danh sach do an
insert into foods(f_id, f_name, f_price)
values ('F1', 'GOI CUON', '170000');

insert into foods(f_id, f_name, f_price)
values ('F2', 'CHA GIO', '160000');

insert into foods(f_id, f_name, f_price)
values ('F3', 'SUP BAP GA', '140000');

insert into foods(f_id, f_name, f_price)
values ('F4', 'XA XIU GA', '200000');

insert into foods(f_id, f_name, f_price)
values ('F5', 'RAU CAI XAO DAU', '190000');

insert into foods(f_id, f_name, f_price)
values ('F6', 'GA SATE LUI', '180000');

insert into foods(f_id, f_name, f_price)
values ('F7', 'TOM LAC BOT', '170000');

insert into foods(f_id, f_name, f_price)
values ('F8', 'MI THAP CAM', '230000');

insert into foods(f_id, f_name, f_price)
values ('F9', 'COM CHIEN', '160000');

insert into foods(f_id, f_name, f_price)
values ('F10', 'SUP NAM ROM CUA', '160000');

insert into foods(f_id, f_name, f_price)
values ('F11', 'SUP BAP CUA', '160000');

insert into foods(f_id, f_name, f_price)
values ('F12', 'BANH MI TOM CHIEN', '150000');

-- Danh sach thuc uong
insert into drinks(d_id, d_name, d_price)
values ('D1', 'CA PHE', '50000');

insert into drinks(d_id, d_name, d_price)
values ('D2', 'NUOC NGOT', '40000');

insert into drinks(d_id, d_name, d_price)
values ('D3', 'NUOC EP CAM', '60000');

insert into drinks(d_id, d_name, d_price)
values ('D4', 'NUOC DUA', '50000');

insert into drinks(d_id, d_name, d_price)
values ('D5', 'SODA CHANH', '50000');

insert into drinks(d_id, d_name, d_price)
values ('D6', 'SODA SUA HOT GA', '60000');

insert into drinks(d_id, d_name, d_price)
values ('D7', 'NUOC EP DUA HAU', '50000');