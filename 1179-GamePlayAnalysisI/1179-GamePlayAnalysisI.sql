-- Last updated: 3/6/2026, 1:49:49 PM
# Write your MySQL query statement below
select player_id , min(event_date) AS first_login
FROM Activity
GROUP BY player_id;