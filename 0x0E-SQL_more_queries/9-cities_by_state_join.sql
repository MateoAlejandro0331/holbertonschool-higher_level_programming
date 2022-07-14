-- lists all cities contained in the database hbtn_0d_us
-- Database pased as an argument
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id;