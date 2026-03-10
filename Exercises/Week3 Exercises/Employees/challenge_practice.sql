/*
## Part 4: Challenge Queries (30 minutes)

### Challenge 4.1

Find employees who earn more than the average salary.
*/


SELECT * FROM employees WHERE salary > (SELECT AVG(salary) from employees);




/*
### Challenge 4.2

List departments that have at least one project.
*/

SELECT * FROM departments WHERE EXISTS(SELECT * FROM projects WHERE departments.dept_id = projects.dept_id);


/*
### Challenge 4.3

Find the employee with the highest salary in each department.
*/
SELECT d.dept_name, MAX(salary) as highest_salary FROM employees e join departments d on e.dept_id = d.dept_id GROUP BY d.dept_id;

/*
### Challenge 4.4

Calculate how long each employee has been with the company (in years and months).
*/

SELECT first_name, last_name, age(CURRENT_DATE, hire_date) as employment_length from employees;