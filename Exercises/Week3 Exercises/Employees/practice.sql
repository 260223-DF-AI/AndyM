/*
### Task 1.1: Add a Column

Add a `phone` column (VARCHAR(20)) to the employees table.
*/
ALTEr TABle employees ADD COLUMN phone VARCHAR(20);
SELECT * FROM employees



/*
### Task 1.2: Modify a Column

Change the `budget` column in departments to allow larger values (DECIMAL(15, 2)).
*/

ALTER TABLE departments ALTER COLUMN budget TYPE DECIMAL(15, 2)


/*
### Task 1.3: Create a New Table

Create a table called `training_courses` with:

- course_id (auto-incrementing primary key)
- course_name (required, VARCHAR(100))
- duration_hours (INTEGER)
- instructor (VARCHAR(100))
*/

CREATE TABLE training_courses(
    course_id SERIAL primary KEY,
    course_name VARCHAR(100) not null,
    duration_hours INT,
    instructor VARCHAR(100)
);


