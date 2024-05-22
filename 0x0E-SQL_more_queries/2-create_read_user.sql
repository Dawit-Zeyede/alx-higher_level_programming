-- create a database and user.
CREATE DATABASE IF NOT EXISTS htbn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_@_pwd';
GRANT SELECT ON 'hbtn_0d_2_pwd';
FLUSH PRIVILEGES;
