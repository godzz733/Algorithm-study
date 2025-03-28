SELECT F.FLAVOR
FROM FIRST_HALF AS F
INNER JOIN (
    SELECT J.FLAVOR, SUM(J.TOTAL_ORDER) AS JULY_TOTAL
    FROM JULY AS J
    GROUP BY J.FLAVOR
) AS C
ON F.FLAVOR = C.FLAVOR
ORDER BY F.TOTAL_ORDER + C.JULY_TOTAL DESC
LIMIT 3;