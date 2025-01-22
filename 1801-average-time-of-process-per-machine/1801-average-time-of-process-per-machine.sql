# Write your MySQL query statement below
Select a.machine_id,
        ROUND(avg(b.timestamp - a.timestamp), 3) AS processing_time
From activity a, activity b
where a.machine_id = b.machine_id
AND a.process_id = b.process_id
AND a.activity_type = "start"
AND b.activity_type = "end"
Group by machine_id

#here we ROUND() it to 3 decimal places 
#timestamp is the column but not the function 