# Write your MySQL query statement below
SELECT today.id
FROM Weather yesterday
JOIN Weather today
ON today.temperature > yesterday.temperature AND datediff( today.recordDate, yesterday.recordDate) = 1;
