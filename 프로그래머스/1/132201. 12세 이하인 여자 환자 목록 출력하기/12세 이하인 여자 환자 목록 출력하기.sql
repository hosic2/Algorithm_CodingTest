-- 코드를 입력하세요
SELECT PT_NAME, PT_NO, GEND_CD, AGE, IFNULL(tlno, 'NONE') as TLNO FROM patient 
where gend_cd = 'W' and AGE < 13
order by 4 desc, 1 asc