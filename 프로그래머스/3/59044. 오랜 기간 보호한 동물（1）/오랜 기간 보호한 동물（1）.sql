-- 코드를 입력하세요
SELECT a.NAME, a.DATETIME 
FROM animal_ins a
left outer join animal_outs b 
USING (ANIMAL_ID)
WHERE b.DATETIME IS NULL
ORDER BY a.DATETIME ASC
LIMIT 3