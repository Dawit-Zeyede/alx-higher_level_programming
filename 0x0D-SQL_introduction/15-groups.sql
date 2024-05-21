-- Number of records with same score in 'secon_table'
SELECT score, COUNT(1) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;
