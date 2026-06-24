import pandas as pd

df=pd.read_csv(
"data/raw/investor_transactions.csv"
)


df['transaction_type']=(
df['transaction_type']
.str.upper()
)


mapping={

'SIP':'SIP',

'LUMPSUM':'Lumpsum',

'REDEMPTION':'Redemption'

}


df['transaction_type']=(
df['transaction_type']
.map(mapping)
)



df=df[df['amount']>0]



df['date']=pd.to_datetime(
df['date'],
errors='coerce'
)



valid=['Verified',
'Pending']


df=df[
df['kyc_status']
.isin(valid)
]



df.to_csv(

"data/processed/transactions_cleaned.csv",

index=False

)

print(df.head())