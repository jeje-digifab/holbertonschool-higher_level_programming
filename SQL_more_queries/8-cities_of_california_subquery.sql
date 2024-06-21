-- Lists all the cities of California that can be found in the database
SELECT cities.id, cities.name
FROM states, cities
WHERE states.name = 'California'
    AND cities.state_id = states.id
ORDER BY cities.name ASC;
