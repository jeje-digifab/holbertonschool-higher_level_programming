-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;

-- Select the database to use
USE hbtn_0c_0;

-- Create the table if it doesn't exist
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- insert values in the table
INSERT INTO second_table (id, name, score )
VALUES
(1,'John', 10),
(2, 'Alex', 3),
(3, "Bob", 14),
(4, 'George', 8);
