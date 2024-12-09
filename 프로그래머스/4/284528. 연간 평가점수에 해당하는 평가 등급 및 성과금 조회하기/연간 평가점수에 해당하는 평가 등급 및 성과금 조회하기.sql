SELECT
    a.EMP_NO,
    a.EMP_NAME,
    b.GRADE,
    CASE 
        WHEN b.GRADE = 'S' THEN a.SAL * 0.2
        WHEN b.GRADE = 'A' THEN a.SAL * 0.15
        WHEN b.GRADE = 'B' THEN a.SAL * 0.1
        ELSE 0
    END AS BONUS
FROM HR_EMPLOYEES a
INNER JOIN (
    SELECT 
        EMP_NO,
        CASE
            WHEN AVG(SCORE) >= 96 THEN 'S'
            WHEN AVG(SCORE) >= 90 THEN 'A'
            WHEN AVG(SCORE) >= 80 THEN 'B'
            ELSE 'C'
        END AS GRADE
    FROM HR_GRADE
    GROUP BY EMP_NO) b
USING (EMP_NO)
ORDER BY 1;
