-- Create the new database if it does not exist already
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use database hbtn_0d_usa
USE hbtn_0d_usa;

-- Script to create states table if it doesn't already exist
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
