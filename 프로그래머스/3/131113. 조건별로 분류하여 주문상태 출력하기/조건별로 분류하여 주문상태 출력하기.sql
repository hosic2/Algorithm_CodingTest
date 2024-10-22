-- 코드를 입력하세요
SELECT order_id, product_id, DATE_FORMAT(out_date, '%Y-%m-%d'),
CASE 
    WHEN out_date <= '2022-05-01' THEN '출고완료'
    WHEN out_date IS NULL THEN '출고미정'
    ELSE '출고대기'
END AS '출고여부'
FROM FOOD_ORDER
ORDER by order_id asc