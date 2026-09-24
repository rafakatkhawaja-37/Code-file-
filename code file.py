import pandas as pd
import numpy as np
import re

def clean_ecommerce_data(file_path):
    print("Loading raw dataset...")
    df = pd.read_excel(file_path, sheet_name="Raw_Data")
    
    # 1. Remove duplicate records
    initial_len = len(df)
    df = df.drop_duplicates().reset_index(drop=True)
    print(f"Removed {initial_len - len(df)} duplicate records.")

    # 2. Standardize Category and Region names
    df["Category"] = df["Category"].astype(str).str.strip().str.title()
    df["Region"] = df["Region"].astype(str).str.strip().str.title()
    df["Region"] = df["Region"].replace("Nan", np.nan)

    # 3. Clean Revenue column (strip currency symbols and commas)
    def clean_currency(val):
        if pd.isna(val) or str(val).strip().lower() == "nan":
            return np.nan
        cleaned_str = re.sub(r"[^\d.]", "", str(val))
        return float(cleaned_str) if cleaned_str else np.nan

    df["Revenue"] = df["Revenue"].apply(clean_currency)

    # 4. Handle invalid/negative quantities
    df.loc[df["Quantity"] < 0, "Quantity"] = np.nan

    # 5. Handle date parsing
    df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

    # Save cleaned data
    output_file = "cleaned_ecommerce_data.csv"
    df.to_csv(output_file, index=False)
    print(f"Data cleaning successfully completed! Saved to '{output_file}'.")

if __name__ == "__main__":
    raw_dataset = "AI + Data_ Make Data Intelligent _ Masterclass 1 _ Practice Dataset (1).xlsx"
    clean_ecommerce_data(raw_dataset)
