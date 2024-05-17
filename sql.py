-- Create a table
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(100),
    salary DECIMAL(10, 2),
    department_id INT
);

-- Insert data into the table
INSERT INTO employees (id, name, position, salary, department_id)
VALUES
    (1, 'Raja', 'Manager', 75000, 1),
    (2, 'Maha', 'Developer', 60000, 2),
    (3, 'Lakshmi', 'Developer', 62000, 2),
    (4, 'Lisa ', 'HR', 50000, 3);

-- Select
SELECT * FROM employees;

-- Update
UPDATE employees
SET salary = 80000
WHERE id = 1;

-- Delete data
DELETE FROM employees
WHERE id = 4;
