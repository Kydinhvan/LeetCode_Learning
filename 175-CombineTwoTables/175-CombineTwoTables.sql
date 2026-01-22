-- Last updated: 1/22/2026, 12:13:00 PM
# Write your MySQL query statement below
SELECT Person.firstName, Person.lastName, Address.city, Address.state 
FROM Person LEFT JOIN Address on Person.personId = Address.personId;

