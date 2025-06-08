select
    customer_name,
    count(*) as total_orders
from {{ ref('int_orders_with_customers') }}
group by customer_name;
