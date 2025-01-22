# Write your MySQL query statement belows
select e.name, eu.unique_id
from Employees e
LEFT JOIN EmployeeUNI eu
ON e.id = eu.id;