import pandas as pd


df=pd.read_csv(

"data/raw/scheme_performance.csv"

)


cols=[

'return_1y',

'return_3y',

'return_5y'

]



for c in cols:

    df[c]=pd.to_numeric(

df[c],

errors='coerce'

)



df['expense_ratio']=(
pd.to_numeric(

df['expense_ratio']

)
)



df=df[

(df['expense_ratio']>=0.1)

&

(df['expense_ratio']<=2.5)

]


df.to_csv(

"data/processed/performance_cleaned.csv",

index=False

)

print(df.head())