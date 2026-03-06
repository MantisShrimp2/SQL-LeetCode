-- Last updated: 3/6/2026, 1:49:58 PM
# Write your MySQL query statement below

DELETE p1 from Person p1, Person P2 WHERE p1.id > p2.id and p1.email = p2.email;