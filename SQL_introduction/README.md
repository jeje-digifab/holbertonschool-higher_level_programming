# SQL Introduction

## Description
This project involves a series of SQL scripts used to manipulate a MySQL database. Each task is associated with a specific script that performs an operation on the database, ranging from creating databases and tables to inserting and manipulating data.

## Requirements
- MySQL installed on your machine
- Administrative access to a MySQL server
- A terminal to execute SQL scripts

## Usage
Each script should be executed via the `mysql` command in a terminal, using an admin user, as follows:

```bash
cat [script_name].sql | mysql -hlocalhost -uroot -p
```

Replace `[script_name]` with the name of the SQL script. For example, to execute the script that creates a database:
```bash
cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
```

## Task List

### 0. List Databases
- **File**: `0-list_databases.sql`
- This script lists all the databases on your MySQL server.

### 1. Create a Database
- **File**: `1-create_database_if_missing.sql`
- This script creates a database named `hbtn_0c_0` if it doesn't already exist.

### 2. Delete a Database
- **File**: `2-remove_database.sql`
- This script deletes the `hbtn_0c_0` database if it exists.

### 3. List Tables
- **File**: `3-list_tables.sql`
- This script lists all tables in a specified database.

### 4. Create First Table
- **File**: `4-first_table.sql`
- This script creates a table called `first_table` in the specified database with two columns: `id` (INT) and `name` (VARCHAR(256)).

### 5. Full Description of Table
- **File**: `5-full_table.sql`
- This script displays the full description (CREATE TABLE structure) of the `first_table`.

### 6. List All Rows in Table
- **File**: `6-list_values.sql`
- This script lists all rows from the `first_table`.

### 7. Insert into Table
- **File**: `7-insert_value.sql`
- This script inserts a new row into the `first_table` with `id=89` and `name='Best School'`.

### 8. Count Rows
- **File**: `8-count_89.sql`
- This script displays the number of rows in the `first_table` where `id` is equal to 89.

### 9. Create Second Table with Multiple Rows
- **File**: `9-full_creation.sql`
- This script creates a new table called `second_table` and inserts multiple rows with names and scores.

### 10. List by Best Score
- **File**: `10-top_score.sql`
- This script lists all rows from the `second_table` in descending order of `score`.

### 11. Select Records with Score >= 10
- **File**: `11-best_score.sql`
- This script displays all rows from `second_table` where `score` is greater than or equal to 10.

### 12. Update Bob's Score
- **File**: `12-no_cheating.sql`
- This script updates Bob’s score in the `second_table` to set it to 10.

### 13. Remove Low Scores
- **File**: `13-change_class.sql`
- This script deletes all rows from the `second_table` where the score is less than or equal to 5.

