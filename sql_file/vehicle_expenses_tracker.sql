# creating database
create database vehicle_expense_analytics;

# database validations
show databases;
SELECT schema_name FROM information_schema.schemata;

# CREATE DATABASE bike_expense_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci; Supports all languages, Avoids encoding issues
use vehicle_expense_analytics;

# creating tables
create table users (
	user_id int primary key,
    user_name varchar(100) not null,
    email varchar(100),
    address varchar(100)
);

create table vehicles (
	vehicle_id int primary key,
    vehicle_model varchar(100) not null,
    brand varchar(100),
    engine_cc int,
    purchase_date date
);

create table locations (
	location_id int primary key,
    location_name varchar(100) not null,
    address varchar(100),
    city varchar(50),
    state varchar(50),
    pincode int
);

create table products (
	product_id int primary key,
    product_name varchar(100) not null,
    category varchar(50),
    is_fuel bit,
    is_service bit
);

create table fuel_price_history (
	fuel_price_id int,
    fuel_price decimal(4,3),
    price_trend_date date
);

create table transactions (
	tranaction_id int primary key,
    user_id int references users(user_id),
    vehicle_id int references vehicle(vehicle_id),
    location_id int references locations(location_id),
    product_id int references products(product_id),
    price decimal(6,3),
    quantity decimal(6,3),
    total_cost decimal(6,3),
    transaction_date date
);

SET SQL_SAFE_UPDATES = 0;

# modifying tables tablenames or columns
# alter table locations rename column pincode to pin_code;
# alter table fuel_price_history modify column fuel_price decimal(8,2);
# alter table transactions rename column tranaction_id to transaction_id;
# alter table transactions modify column price decimal(8,2);
# alter table transactions modify column quantity decimal(8,2);
# alter table transactions modify column total_cost decimal(8,2);

# alter table vehicle_expense_analytics.users add column modified_date datetime default current_timestamp on update current_timestamp;
# alter table vehicle_expense_analytics.vehicles add column modified_date datetime default current_timestamp on update current_timestamp;
# alter table vehicle_expense_analytics.locations add column modified_date datetime default current_timestamp on update current_timestamp;
# alter table vehicle_expense_analytics.products add column modified_date datetime default current_timestamp on update current_timestamp;
# alter table vehicle_expense_analytics.fuel_price_history add column modified_date datetime default current_timestamp on update current_timestamp;
# alter table vehicle_expense_analytics.transactions add column modified_date datetime default current_timestamp on update current_timestamp;

# alter table users modify column email varchar(100) unique;
# desc vehicle_expense_analytics.users;
# alter table vehicle_expense_analytics.locations rename column address to locality;
# alter table vehicle_expense_analytics.products add column brand varchar(100) after product_name;

# verifying uploaded data
SELECT * FROM vehicle_expense_analytics.users;
SELECT * FROM vehicle_expense_analytics.vehicles;
SELECT * FROM vehicle_expense_analytics.locations;
SELECT * FROM vehicle_expense_analytics.products;
SELECT * FROM vehicle_expense_analytics.fuel_price_history;
SELECT * FROM vehicle_expense_analytics.transactions;

# select * from vehicle_expense_analytics.transactions where user_id is null or vehicle_id is null or location_id is null or product_id is null;
with expenses_comparison as (select price, quantity, round(total_cost,0) as rounded_total_cost, round((price * quantity),0) as total_exp, 
case 
	when round(total_cost,0) = round((price * quantity),0) then 1
    when round(total_cost,0) != round((price * quantity),0) then 0
    end as comparison_result
 from vehicle_expense_analytics.transactions)
select * from expenses_comparison where comparison_result = 0;
select * from vehicle_expense_analytics.transactions where price < 0 or quantity < 0 or total_cost < 0;


# Modifying records
# update vehicle_expense_analytics.users set  email = "kishorekumarys.98@gmail.com" where user_id = 1;
# update vehicle_expense_analytics.locations set address = null where address = 'Nan';
# update vehicle_expense_analytics.transactions set price = 102.92 where price = 102.93;
# update vehicle_expense_analytics.products set product_name = 'Helmet Skull Cap' where product_name = 'Helmet Cap';
# update vehicle_expense_analytics.products set brand = 'Regular' where product_name = 'Petrol';
# update vehicle_expense_analytics.products set brand = 'Vega Bunny Bolt' where product_name = 'Helmet';
# update vehicle_expense_analytics.products set brand = 'ICICI' where product_name = 'Icici Insurance';
# update vehicle_expense_analytics.products set brand = 'MRF' where product_name = 'Tyres';
# update vehicle_expense_analytics.products set brand = 'ICICI' where product_name = 'Icici Insurance';
# update vehicle_expense_analytics.products set brand = 'Amaron' where product_name = 'Battery';
# update vehicle_expense_analytics.products set product_name = 'Full Face Helmet' where product_name = 'Helmet';
# Insert into vehicle_expense_analytics.products (product_id, product_name, brand, category, is_fuel, is_service) values (17, 'Half Face Helmet','Vega', 'Safety Gear',0,0), (18, 'Skull Cap Helmet',null, 'Safety Gear',0,0);
# update vehicle_expense_analytics.transactions set product_id = 18 where transaction_id = 21;
# update vehicle_expense_analytics.transactions set product_id = 17 where transaction_id = 3;


# backup
# mysqldump -h localhost -u root -p vehicle_expense_analytics > D:\Project\Vehicle-Data-Analysis\database_backup\vehicle_expense_analytics.sql

# create index on transaction table
create index idx_transaction_id on vehicle_expense_analytics.transactions(transaction_id);
create index idx_transaction_date on vehicle_expense_analytics.transactions(transaction_date);
create index idx_transaction_total_cost on vehicle_expense_analytics.transactions(total_cost);


# create important view

create view v_bike_expenses_metrics as (
select t.transaction_date,  v.vehicle_model, l.location_name, l.locality, l.city, l.state, l.pin_code, p.product_name, p.brand, p.category, p.is_fuel, t.price, t.quantity, t.total_cost 
from vehicle_expense_analytics.transactions t 
left join vehicle_expense_analytics.users u on t.transaction_id = u.user_id
left join vehicle_expense_analytics.vehicles v on t.vehicle_id = v.vehicle_id
left join vehicle_expense_analytics.locations l on t.location_id = l.location_id
left join vehicle_expense_analytics.products p on t.product_id = p.product_id);

# drop view v_bike_expenses_metrics;
select * from v_bike_expenses_metrics;

# create quick access store procesures
