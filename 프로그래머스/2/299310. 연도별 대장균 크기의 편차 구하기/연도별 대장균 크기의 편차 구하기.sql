WITH max_value AS (
    SELECT YEAR(DIFFERENTIATION_DATE) AS YEAR, MAX(SIZE_OF_COLONY) AS MAX_VALUE
    FROM ECOLI_DATA
    GROUP BY 1
)
SELECT 
    YEAR(a.DIFFERENTIATION_DATE) AS YEAR,
    b.MAX_VALUE - a.SIZE_OF_COLONY AS YEAR_DEV,
    a.ID
FROM ECOLI_DATA a
INNER JOIN max_value b
ON YEAR(a.DIFFERENTIATION_DATE) = b.YEAR
ORDER BY 1, 2;