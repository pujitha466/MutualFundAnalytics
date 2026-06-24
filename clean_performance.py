import pandas as pd

# Read dataset
df = pd.read_csv("data/raw/07_scheme_performance.csv")

# Remove spaces from column names
df.columns = df.columns.str.strip()

print("Columns found:")
print(df.columns.tolist())


# -------------------------
# Find return columns
# -------------------------

return_cols = []

for c in df.columns:
    if "return" in c.lower():
        return_cols.append(c)


print("\nReturn columns:")
print(return_cols)


# Convert returns to numeric

for c in return_cols:
    df[c] = pd.to_numeric(df[c], errors="coerce")


# -------------------------
# Expense Ratio
# -------------------------

expense_col = None

for c in df.columns:
    if "expense" in c.lower():
        expense_col = c
        break


if expense_col is not None:

    df[expense_col] = pd.to_numeric(
        df[expense_col],
        errors="coerce"
    )

    anomalies = df[
        (df[expense_col] < 0.1)
        |
        (df[expense_col] > 2.5)
    ]

    print("\nExpense ratio anomalies")

    print(anomalies.shape[0])



# -------------------------
# Save cleaned file
# -------------------------

df.to_csv(

    "data/processed/07_scheme_performance_cleaned.csv",

    index=False

)



print("\nCleaning completed")

print(df.head())

print(df.shape)
