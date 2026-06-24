import requests


import pandas as pd


url="https://api.mfapi.in/mf/125497"


r=requests.get(url)


data=r.json()



df=pd.DataFrame(

data['data']

)



df.to_csv(

'data/raw/hdfc_top100.csv',

index=False

)


print(df.head())
