-- Create a departments table
CREATE TABLE departments (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

-- Insert data
INSERT INTO departments (id, name)
VALUES
    (1, 'Sales'),
    (2, 'Development'),
    (3, 'Human Resources');

-- Inner Join
SELECT
    e.name AS employee_name,
    d.name AS department_name
FROM
    employees e
JOIN
    departments d ON e.department_id = d.id;

-- Left Join
SELECT
    e.name AS employee_name,
    d.name AS department_name
FROM
    employees e
LEFT JOIN
    departments d ON e.department_id = d.id;

-- Right Join
SELECT
    e.name AS employee_name,
    d.name AS department_name
FROM
    employees e
RIGHT JOIN
    departments d ON e.department_id = d.id;

-- Full Outer Join
SELECT
    e.name AS employee_name,
    d.name AS department_name
FROM
    employees e
FULL OUTER JOIN
    departments d ON e.department_id = d.id;
