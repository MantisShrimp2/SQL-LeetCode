-- Last updated: 3/6/2026, 1:50:00 PM
# Write your MySQL query statement below
SELECT name as Customers
from Customers
Where id not in (
    select customerId
    from Orders
);