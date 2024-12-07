SELECT COUNT(a.ID) AS FISH_COUNT
FROM FISH_INFO a
INNER JOIN FISH_NAME_INFO b
USING(FISH_TYPE)
WHERE b.FISH_NAME IN ("BASS", "SNAPPER");