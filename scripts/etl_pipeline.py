import pandas as pd

def etl_pipeline():
    # -------------------
    # 1️⃣ Extract
    # -------------------
    df = pd.read_csv("data/Warehouse_and_Retail_Sales - Copy.csv")
    
    # -------------------
    # 2️⃣ Transform
    # -------------------
    # Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    
    # Fill missing numeric values
    numeric_cols = ["retail_sales","retail_transfers","warehouse_sales"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = df[col].fillna(0)
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Create date column
    df["date"] = pd.to_datetime(df["year"].astype(str) + "-" + df["month"].astype(str) + "-01")
    
    # -------------------
    # 3️⃣ Load
    # -------------------
    df.to_csv("data/cleaned_sales.csv", index=False)
    print("✅ ETL pipeline completed successfully!")

# Run ETL pipeline
if __name__ == "__main__":
    etl_pipeline()