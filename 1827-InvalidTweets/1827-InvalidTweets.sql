-- Last updated: 1/22/2026, 12:12:44 PM
# Write your MySQL query statement below
select tweet_id from Tweets
where CHAR_LENGTH(content) >15 