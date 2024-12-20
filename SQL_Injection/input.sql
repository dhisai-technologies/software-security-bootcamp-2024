-- Test Case 1: Multiple WHERE conditions (complex AND/OR)
SELECT * 
FROM employees
WHERE (department = 'HR' OR department = 'Finance')
AND (salary > 50000 OR salary < 40000)
AND (joining_date BETWEEN '2020-01-01' AND '2023-01-01' OR joining_date IS NULL);

-- Test Case 2: Dynamic JOIN conditions
SELECT * 
FROM orders
JOIN customers 
    ON orders.customer_id = customers.id
    AND orders.order_date = customers.registration_date
    AND customers.status = 'active'
LEFT JOIN products
    ON orders.product_id = products.id 
    AND products.price > 100;

-- Test Case 3: Subquery Construction (nested subqueries)
SELECT employee_id, name, 
    (SELECT MAX(salary) FROM salaries WHERE employee_id = employees.employee_id AND year = 2023) AS max_salary
FROM employees
WHERE department = 'Engineering' 
    AND (SELECT COUNT(*) FROM projects WHERE employee_id = employees.employee_id) > 5
ORDER BY name;

-- Test Case 4: Complex WHERE conditions with nested queries
SELECT * 
FROM students 
WHERE age > 18 
  AND (SELECT COUNT(*) FROM enrollments WHERE student_id = students.id) > 3
  AND EXISTS (SELECT 1 FROM courses WHERE course_id = enrollments.course_id AND course_name = 'Math');
