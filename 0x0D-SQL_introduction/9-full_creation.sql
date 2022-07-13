-- Full create table
-- The database name will be passed as an argument
CREATE TABLE IF NOT EXISTS second_table (
    id int,
    name VARCHAR(256),
    score INT
);
INSERT INTO second_table
    (id, name, score) 
VALUES 
    (1,"John", 10),
    (2,"Alex", 3),
    (3,"Bob", 14),
    (4, "George", 8);