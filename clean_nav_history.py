import pandas as pd

df=pd.read_csv("data/raw/nav_history.csv")

df['date']=pd.to_datetime(df['date'],
errors='coerce')


df=df.dropna(subset=['date'])


df=df.sort_values(
['scheme_code','date']
)


df['nav']=(
df.groupby('scheme_code')
['nav']
.ffill()
)


df=df.drop_duplicates()


df=df[df['nav']>0]


df.to_csv(
"data/processed/nav_history_cleaned.csv",
index=False
)


print(df.head())