-- sql cript to import database
-- a SQL script that ranks country origins of bands,
-- ordered by the number of (non-unique) fans
SELECT RANK() OVER(ORDER BY COUNT(*) DESC) AS
origin,
COUNT(*) AS nb_fans
FROM metal_bands
GROUP BY city;
