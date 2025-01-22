# Write your MySQL query statement below
select s.student_id, s.student_name, su.subject_name, COUNT(E.student_id) as attended_exams
from Students s
CROSS JOIN Subjects su
Left join Examinations e 
on s.student_id = e.student_id AND su.subject_name = e.subject_name
Group BY s.student_id , s.student_name, su.subject_name
Order BY s.student_id , s.student_name, su.subject_name;