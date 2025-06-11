SELECT a.ANIMAL_ID, a.NAME FROM ANIMAL_INS a
INNER JOIN ANIMAL_OUTS b
USING (ANIMAL_ID)
WHERE a.datetime > b.datetime
order by a.datetime asc