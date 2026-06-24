SELECT *
FROM fact_nav
LIMIT 5;


SELECT AVG(nav)
FROM fact_nav;



SELECT MAX(nav)
FROM fact_nav;



SELECT MIN(nav)
FROM fact_nav;



SELECT *
FROM fact_performance
WHERE expense_ratio<1;



SELECT SUM(amount)
FROM fact_transactions
WHERE transaction_type='SIP';



SELECT COUNT(*)
FROM fact_transactions;



SELECT transaction_type,
COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;



SELECT AVG(expense_ratio)
FROM fact_performance;



SELECT *
FROM fact_performance;