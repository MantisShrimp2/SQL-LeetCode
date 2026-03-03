-- Last updated: 3/3/2026, 9:27:10 AM
# Write your MySQL query statement below
SELECT email from Person
GROUP BY email 
HAVING COUNT(email) > 1;
