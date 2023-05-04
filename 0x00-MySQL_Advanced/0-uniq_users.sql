-- a SQL script that creates a table users
--attr: id (int), name (string), email (string)

CREATE TABLE users IF NOT EXISTS (
    id int NOT NULL AUTO_INCREMENT,
    name char(255),
    email varchar(255) NOT NULL UNIQUE,
    PRIMARY KEY (id)
);