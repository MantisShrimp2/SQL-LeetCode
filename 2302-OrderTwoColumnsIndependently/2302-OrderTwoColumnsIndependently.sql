-- Last updated: 3/6/2026, 11:59:17 AM
WITH first_ordered AS (
    SELECT first_col, ROW_NUMBER() OVER (ORDER BY first_col ASC) AS rn
    FROM Data
),
second_ordered AS (
    SELECT second_col, ROW_NUMBER() OVER (ORDER BY second_col DESC) AS rn
    FROM Data
)
SELECT first_col, second_col
FROM first_ordered
JOIN second_ordered ON first_ordered.rn = second_ordered.rn