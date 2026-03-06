-- Last updated: 3/6/2026, 1:49:48 PM
# Write your MySQL query statement below
select player_id, device_id FROM Activity
WHERE (player_id, event_date) IN
(select player_id , min(event_date) AS first_login
FROM Activity
GROUP BY player_id);