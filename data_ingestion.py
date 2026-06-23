import pandas as pd
import os

path = "data/raw"

files = os.listdir(path)

for file in files:
    if file.endswith(".csv"):

        print("\n" + "="*60)
        print("File Name:", file)

        df = pd.read_csv(os.path.join(path, file))

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())