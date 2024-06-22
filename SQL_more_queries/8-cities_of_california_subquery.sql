--  lists all the cities of California that can be found in the database
SELECT id
FROM states
WHERE name = 'California';

SELECT *
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;