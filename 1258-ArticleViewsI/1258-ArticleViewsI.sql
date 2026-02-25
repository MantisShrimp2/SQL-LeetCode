-- Last updated: 2/25/2026, 3:18:13 PM
# Write your MySQL query statement below
select Distinct author_id as id from Views where author_id = viewer_id
Order by author_id;