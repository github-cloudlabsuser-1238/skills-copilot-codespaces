-- create a table with 5 coloumns customer_id, customer_fname, customer_lname, customer_phone, customer_address
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_fname VARCHAR(50),
    customer_lname VARCHAR(50),
    customer_phone VARCHAR(15),
    customer_address VARCHAR(100)
);

-- fill in 5 rows in customers table
INSERT INTO customers (customer_id, customer_fname, customer_lname, customer_phone, customer_address) VALUES
(1, 'John', 'Doe', '123-456-7890', '123 Main St, New York, NY 10001'),
(2, 'Jane', 'Doe', '123-456-7891', '124 Main St, New York, NY 10001'),
(3, 'Alice', 'Smith', '123-456-7892', '125 Main St, New York, NY 10001'),
(4, 'Bob', 'Johnson', '123-456-7893', '126 Main St, New York, NY 10001'),
(5, 'Charlie', 'Brown', '123-456-7894', '127 Main St, New York, NY 10001');


-- show the data in customers table
SELECT * FROM customers;