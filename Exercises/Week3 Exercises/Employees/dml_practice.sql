/*
### Task 2.1: INSERT Operations

Add 3 new employees to the HR department:

- Grace Lee, <grace.lee@company.com>, salary 58000
- Ivan Chen, <ivan@company.com>, salary 61000
- Julia Kim, <julia@company.com>, salary 55000

```sql
-- Your query here
```
*/
INSERT INTO employees(first_name, last_name, email, salary)
VALUES 
('Grace','Lee', 'grace.lee@company.com', 58000),
('Ivan','Chen', 'ivan@company.com', 61000),
('Julia','Kim', 'julia@company.com', 55000);

-- forgot to change dept to HR
UPDATE employees set dept_id = 3 WHERE emp_id = 9 or emp_id = 10 or emp_id = 11;


/*
### Task 2.2: UPDATE Operations

A) Give all Engineering department employees a 10% raise:

```sql
-- Your query here
```

B) Update Bob Smith's email to <bob.smith@company.com>:

```sql
-- Your query here
```
*/

UPDATE employees set salary = salary * 1.1 WHERE dept_id = 1;



/*
### Task 2.3: DELETE Operations

A) Delete all projects that have already ended (end_date before today):

```sql
-- Your query here
```
*/

SELECT * FROM projects;
DELETE FROM projects WHERE end_date < CURRENT_DATE;

SELECT * FROM projects;

/*
B) **CAREFUL!** Write (but don't run) a DELETE that would remove all employees without a department. What makes this dangerous?

```sql
-- Your query here (don't run!)
-- Explain why this could be dangerous:
```

---
*/

DELETE FROM employees WHERE dept_id = NULL

-- trying to compare anything to NULL is dangerous, behavior could be not as we expect it

-- ans from online: Comparing anything to Null is dangerous because it results in "UKNOWN" rather than true or false meaning it won't match to anything
