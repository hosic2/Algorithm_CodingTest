SELECT 
    YEAR(b.SALES_DATE) AS YEAR, 
    MONTH(b.SALES_DATE) AS MONTH, 
    COUNT(DISTINCT a.USER_ID) AS PURCHASED_USERS, 
    ROUND(COUNT(DISTINCT a.USER_ID) / (SELECT COUNT(*) FROM USER_INFO WHERE YEAR(JOINED) = 2021), 1) AS PURCHASED_RATIO
FROM USER_INFO a
INNER JOIN ONLINE_SALE b
    ON a.USER_ID = b.USER_ID
WHERE YEAR(a.JOINED) = '2021'
GROUP BY 1, 2
ORDER BY 1, 2;