WITH value AS (
    SELECT 
        car.daily_fee,
        car.car_type,
        his.history_id,
        DATEDIFF(his.end_date, his.start_date) + 1 AS period,
        CASE 
            WHEN DATEDIFF(his.end_date, his.start_date) + 1 >= 90 THEN '90일 이상'
            WHEN DATEDIFF(his.end_date, his.start_date) + 1 >= 30 THEN '30일 이상'
            WHEN DATEDIFF(his.end_date, his.start_date) + 1 >= 7  THEN '7일 이상'
            ELSE 'NONE'
        END AS duration_type
    FROM car_rental_company_rental_history AS his
    INNER JOIN car_rental_company_car AS car 
        ON car.car_id = his.car_id
    WHERE car.car_type = '트럭'
)

SELECT 
    v.history_id, 
    ROUND(v.daily_fee * v.period * (100 - IFNULL(p.discount_rate, 0)) / 100) AS fee
FROM value AS v
LEFT JOIN car_rental_company_discount_plan AS p 
    ON p.duration_type = v.duration_type 
   AND p.car_type = v.car_type
ORDER BY fee DESC, v.history_id DESC;