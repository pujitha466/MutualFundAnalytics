import pandas as pd



df=pd.read_csv(

'data/raw/08_investor_transactions.csv'

)



df['transaction_date']=pd.to_datetime(

df['transaction_date']

)



df['transaction_type']=df[

'transaction_type'

].str.title()



df=df[

df['amount_inr']>0

]



df=df[

df['kyc_status'].notnull()

]



df.to_csv(

'data/processed/transactions_cleaned.csv',

index=False

)



print(df.head())
