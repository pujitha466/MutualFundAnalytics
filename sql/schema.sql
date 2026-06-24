CREATE TABLE dim_fund(

amfi_code INTEGER PRIMARY KEY,

scheme_name TEXT,

fund_house TEXT,

category TEXT,

plan TEXT,

risk_grade TEXT,

expense_ratio REAL

);



CREATE TABLE fact_nav(

amfi_code INTEGER,

date DATE,

nav REAL

);



CREATE TABLE fact_transactions(

investor_id TEXT,

transaction_date DATE,

amfi_code INTEGER,

transaction_type TEXT,

amount_inr REAL,

state TEXT,

city TEXT,

city_tier TEXT,

age_group TEXT,

gender TEXT,

annual_income_lakh REAL,

payment_mode TEXT,

kyc_status TEXT

);



CREATE TABLE fact_performance(

amfi_code INTEGER,

return_1yr REAL,

return_3yr REAL,

return_5yr REAL,

benchmark_return REAL,

alpha REAL,

beta REAL,

sharpe_ratio REAL,

sortino_ratio REAL,

std_dev REAL,

max_drawdown REAL,

aum_crore REAL,

expense_ratio REAL,

morningstar_rating INTEGER

);
