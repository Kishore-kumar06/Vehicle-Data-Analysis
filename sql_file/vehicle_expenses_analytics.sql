# create important view

create view v_bike_expenses_metrics as (
select t.transaction_date,  v.vehicle_model, l.location_name, l.locality, l.city, l.state, l.pin_code, p.product_name, p.brand, p.category, p.is_fuel, t.price, t.quantity, t.total_cost 
from vehicle_expense_analytics.transactions t 
left join vehicle_expense_analytics.users u on t.transaction_id = u.user_id
left join vehicle_expense_analytics.vehicles v on t.vehicle_id = v.vehicle_id
left join vehicle_expense_analytics.locations l on t.location_id = l.location_id
left join vehicle_expense_analytics.products p on t.product_id = p.product_id);

# drop view v_bike_expenses_metrics;
#select * from v_bike_expenses_metrics;

select t.transaction_date, 
monthname(t.transaction_date) as transaction_month, 
year(t.transaction_date) as transaction_year,  
l.location_name, 
l.locality, 
l.city, 
l.state,  
p.product_name, 
p.brand, 
p.category, 
p.is_fuel, 
t.price, 
t.quantity, 
t.total_cost,
sum(t.total_cost) over(order by t.transaction_id) as cum_total_cost,
sum(case when p.is_fuel = 1 then t.quantity else 0 end) over(order by t.transaction_id) as cum_fuel_quantity
from vehicle_expense_analytics.transactions t 
left join vehicle_expense_analytics.users u on t.transaction_id = u.user_id
left join vehicle_expense_analytics.vehicles v on t.vehicle_id = v.vehicle_id
left join vehicle_expense_analytics.locations l on t.location_id = l.location_id
left join vehicle_expense_analytics.products p on t.product_id = p.product_id;