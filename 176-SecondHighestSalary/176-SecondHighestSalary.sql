-- Last updated: 3/6/2026, 1:50:03 PM
# Write your MySQL query statement below
SELECT(SELECT DISTINCT
    Salary 
FROM
    Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 1)AS SecondHighestSalary;