# Write your MySQL query statement below
select id, movie, description, rating
from Cinema
where description != 'boring' AND mod(id,2) = 1
order by rating DESC;