/*
### Basic Queries

**Query 3.1:** List all employees ordered by salary (highest first)

```sql
-- Your query here
```
*/
SELECT * FROM employees ORDER BY salary desc;
/*
**Query 3.2:** Find all employees in the Engineering department

```sql
-- Your query here
```
*/
SELECT * FROM employees WHERE dept_id = 1;



/*
**Query 3.3:** List employees hired in 2021 or later

```sql
-- Your query here
```
*/
SELECT * FROM employees WHERE EXTRACT(YEAR from hire_date) >= '2021';



/*
### Filtering and Operators

**Query 3.4:** Find employees with salary between 60000 and 80000

```sql
-- Your query here
```
*/
SELECT * FROM employees WHERE salary >=60000 and salary <=80000;

/*
**Query 3.5:** Find employees whose email contains 'company'

```sql
-- Your query here
```
*/
SELECT * FROM employees WHERE email LIKE '%' || 'company' || '%';



/*
**Query 3.6:** List departments in Buildings A or B

```sql
-- Your query here
```
*/

SELECT * FROM departments WHERE location = 'Building A' or location = 'Building B';

/*
### Aggregate Functions

**Query 3.7:** Calculate the total salary expense per department

```sql
-- Your query here
```
*/
SELECT d.dept_name,SUM(salary) as total_salary_expense from employees e JOIN departments d on e.dept_id = d.dept_id GROUP BY d.dept_id;


/*
**Query 3.8:** Find the average, minimum, and maximum salary

```sql
-- Your query here
```
*/

SELECT MAX(salary) as max_salary, MIN(salary) as min_salary, AVG(salary) as avg_salary FROM employees;

/*
**Query 3.9:** Count employees in each department, only show departments with 2+ employees

```sql
-- Your query here
```
*/
SELECT d.dept_name, COUNT(*) as num_employees from employees e JOIN departments d on e.dept_id = d.dept_id GROUP BY d.dept_id HAVING COUNT(*) > 2;



/*
### Aliases and Formatting

**Query 3.10:** Create a report showing full name (first + last), department name, and formatted salary

```sql
-- Your query here
-- Expected output columns: full_name, department, salary_formatted
```

---
*/

SELECT first_name, last_name, dept_name, salary FROM employees JOIN departments on employees.dept_id = departments.dept_id;