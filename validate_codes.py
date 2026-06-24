import pandas as pd


fund=pd.read_csv(

'data/raw/01_fund_master.csv'

)


nav=pd.read_csv(

'data/raw/02_nav_history.csv'

)



missing=~fund['amfi_code'].isin(

nav['amfi_code']

)


print(

fund[missing]

)
