-- 코드를 입력하세요
SELECT CONCAT("/home/grep/src/", B.BOARD_ID, "/", G.FILE_ID, G.FILE_NAME, G.FILE_EXT) AS FILE_PATH FROM USED_GOODS_BOARD B
JOIN USED_GOODS_FILE G
USING (BOARD_ID)
WHERE B.VIEWS = (SELECT MAX(VIEWS) FROM USED_GOODS_BOARD)
ORDER BY G.FILE_ID DESC;