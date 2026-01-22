-- Last updated: 1/22/2026, 12:12:57 PM
# Write your MySQL query statement below
Select e1.name as Employee From Employee as e1, Employee as e2
Where e1.managerId = e2.Id and e1.salary > e2.salary;
# table  