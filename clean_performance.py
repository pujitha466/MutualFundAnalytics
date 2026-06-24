import pandas as pd



df=pd.read_csv(

'data/raw/07_scheme_performance.csv'

)



cols=[

'return_1yr_pct',

'return_3yr_pct',

'return_5yr_pct'

]



for c in cols:


    df[c]=pd.to_numeric(

df[c],

errors='coerce'

)



df['negative_sharpe']=df[

'sharpe_ratio'

]<0



df=df[

(df['expense_ratio_pct']>=0.1)

&

(df['expense_ratio_pct']<=2.5)

]



df.to_csv(

'data/processed/performance_cleaned.csv',

index=False

)



print(df.head())

