-- List all records of 'second_table'
SELECT score, name
FROM second_table
HAVING name IS NOT NULL
ORDER BY score DESC
