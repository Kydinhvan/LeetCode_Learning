-- Last updated: 1/22/2026, 12:12:49 PM
# Write your MySQL query statement below
select id, movie, description, rating from Cinema 
where id % 2 != 0 and description !="boring"
order by rating DESC