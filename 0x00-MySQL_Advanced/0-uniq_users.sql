-- a SQL script that creates a table users
--attr: id (int), name (string), email (string)

CREATE TABLE users IF NOT EXISTS (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name varchar(255),
    email varchar(255) NOT NULL UNIQUE,
    );