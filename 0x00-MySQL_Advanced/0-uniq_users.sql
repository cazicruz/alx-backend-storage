-- a SQL script that creates a table users
--attr: id (int), name (string), email (string)

CREATE TABLE users IF NOT EXISTS (
    id INT NOT NULL AUTO_INCREMENT,
    name CHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    PRIMARY KEY (id)
);