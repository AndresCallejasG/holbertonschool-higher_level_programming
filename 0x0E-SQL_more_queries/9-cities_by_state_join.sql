-- SQL - More queries
-- lists all the cities of California that can be found in the database using join
SELECT cities.id, cities.name, states.name
    FROM cities JOIN states ON cities.id = states.id
    ORDER BY cities.id; 
