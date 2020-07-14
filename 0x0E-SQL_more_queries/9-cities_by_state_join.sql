-- SQL - More queries
-- lists all the cities of California that can be found in the database using join
SELECT cities.id, cities.name, states.name
    FROM cities JOIN states ON states.id = cities.state_id
    ORDER BY cities.id; 
