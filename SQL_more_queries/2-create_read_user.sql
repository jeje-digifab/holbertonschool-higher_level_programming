-- Create hbtn_0d_2 database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create MySQL user user_0d_2 if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privileges to the user user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Apply the privilege changes
FLUSH PRIVILEGES;
