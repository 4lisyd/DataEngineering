with source as (
    select * from {{ source('raw', 'customers') }}
),
cleaned as (
    select
        customer_id,
        customer_name
    from source
)
select * from cleaned;
