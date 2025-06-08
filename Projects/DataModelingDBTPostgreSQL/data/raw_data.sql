-- Example raw orders table
CREATE TABLE raw.orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date TEXT
);

INSERT INTO raw.orders VALUES
(1, 101, '2024-01-01'),
(2, 102, '2024-01-02'),
(3, 101, '2024-01-03');

-- Example raw customers table
CREATE TABLE raw.customers (
    customer_id INT PRIMARY KEY,
    customer_name TEXT
);

INSERT INTO raw.customers VALUES
(101, 'Alice'),
(102, 'Bob');
