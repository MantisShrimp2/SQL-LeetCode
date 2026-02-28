-- Last updated: 2/28/2026, 6:04:23 PM
# Write your MySQL query statement below
SELECT customer_id FROM Customers
WHERE year = 2021
AND revenue > 0.0
ORDER BY revenue DESC;