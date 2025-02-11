SELECT a.MEMBER_NAME, b.REVIEW_TEXT, DATE_FORMAT(b.REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM MEMBER_PROFILE a
INNER JOIN REST_REVIEW b
USING (MEMBER_ID)
INNER JOIN (SELECT MEMBER_ID, COUNT(*) FROM REST_REVIEW GROUP BY MEMBER_ID ORDER BY 2 DESC LIMIT 1) c
USING (MEMBER_ID)
ORDER BY REVIEW_DATE, REVIEW_TEXT;

