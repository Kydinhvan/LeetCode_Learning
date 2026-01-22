-- Last updated: 1/22/2026, 12:12:42 PM
# Write your MySQL query statement below
# first order = min(order_date) for each cystomer id -> identify
# count first order = customer_pref_delivery_date 
# count / total 

select
round(
    100.0*sum( case when order_date = customer_pref_delivery_date then 1 else 0 end ) / count(*)
    ,2) 
as immediate_percentage 
from Delivery
where (customer_id, order_date) in 
(
    select customer_id, min(order_date) as f_order_date
    from Delivery
    group by customer_id
);
