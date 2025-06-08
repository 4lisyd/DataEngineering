with orders as (
    select * from {{ ref('stg_orders') }}
),
customers as (
    select * from {{ ref('stg_customers') }}
)
select
    o.order_id,
    o.order_date,
    c.customer_name
from orders o
join customers c on o.customer_id = c.customer_id;
