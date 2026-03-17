import pandas as pd

# load dataset
df = pd.read_csv("data/Warehouse_and_Retail_Sales.csv")

print("Initial shape:", df.shape)

# standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# check missing values
print("\nMissing values:\n", df.isnull().sum())

# fill missing numeric values
numeric_cols = ["retail_sales", "retail_transfers", "warehouse_sales"]
for col in numeric_cols:
    if col in df.columns:
        df[col] = df[col].fillna(0)

# remove duplicates
df = df.drop_duplicates()

# create date column
df["date"] = pd.to_datetime(df["year"].astype(str) + "-" + df["month"].astype(str) + "-01")

print("Final shape:", df.shape)

# save cleaned data
df.to_csv("data/cleaned_sales.csv", index=False)

print("✅ Data cleaned successfully!")
