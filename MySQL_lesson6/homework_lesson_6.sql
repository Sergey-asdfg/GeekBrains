use vk;

-- Task 1:

SELECT * FROM messages WHERE from_user_id = 1 or to_user_id = 1;

-- Answer: 2 messages, from 1 to 100 and from 100 to 1

-- Task 2:

SELECT 
	COUNT(*) as cnt,
	user_id
FROM likes
WHERE user_id IN (SELECT user_id FROM profiles WHERE (birthday + INTERVAL 10 YEAR) > now())
GROUP BY user_id
WITH ROLLUP;

-- Answer: 25

-- Task 3:

SELECT 
	COUNT(*) as cnt,
	user_id
FROM likes
WHERE user_id IN (SELECT user_id FROM profiles WHERE gender = 'M')
GROUP BY user_id
WITH ROLLUP;

-- 44 likes from male

SELECT 
	COUNT(*) as cnt,
	user_id
FROM likes
WHERE user_id IN (SELECT user_id FROM profiles WHERE gender = 'F')
GROUP BY user_id
WITH ROLLUP;

-- 56 likes from female

-- Answer: from Female is more.
