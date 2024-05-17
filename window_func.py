-- Calculate the average salary per department and show the difference from the average
SELECT
    name,
    position,
    salary,
    department_id,
    AVG(salary) OVER (PARTITION BY department_id) AS avg_salary,
    salary - AVG(salary) OVER (PARTITION BY department_id) AS salary_diff
FROM
    employees;
