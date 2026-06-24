SELECT COUNT(*)
FROM dim_fund;



SELECT AVG(nav)
FROM fact_nav;



SELECT MAX(nav)
FROM fact_nav;



SELECT MIN(nav)
FROM fact_nav;



SELECT transaction_type,
COUNT(*)

FROM fact_transactions

GROUP BY transaction_type;



SELECT AVG(return_3yr_pct)

FROM fact_performance;



SELECT DISTINCT(category)

FROM dim_fund;



SELECT *

FROM fact_nav

LIMIT 10;



SELECT *

FROM fact_transactions

LIMIT 10;



SELECT *

FROM fact_performance

LIMIT 10;
