SELECT first_name, second_name, last_name, department, user_id
FROM Teachers t
JOIN Users p ON t.user_id = p.id
WHERE p.first_name = 