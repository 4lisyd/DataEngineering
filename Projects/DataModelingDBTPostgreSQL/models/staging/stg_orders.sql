with source as (
    select * from {{ source('raw', 'orders') }}
),
cleaned as (
    select
        order_id,
        customer_id,
        order_date::date as order_date
    from source
)
select * from cleaned;
