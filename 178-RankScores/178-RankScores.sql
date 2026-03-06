-- Last updated: 3/6/2026, 1:50:02 PM
# Write your MySQL query statement below
SELECT S1.Score, (
    SELECT COUNT(DISTINCT Score) FROM Scores Where Score >= S1.Score) AS 'rank'
FROM Scores S1
ORDER BY S1.Score DESC