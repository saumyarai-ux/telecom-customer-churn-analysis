import pandas as pd
import numpy as np
# Mocking raw, messy customer transaction data
raw_data = {
   'Customer_ID':,
   'Monthly_Charges': ['$85.50', '95.00', '   ', '$115.20', '70.40'],
   'Contract_Type': ['Month-to-month', 'Two year', 'Month-to-month', None, 'One year'],
   'Churn': ['Yes', 'No', 'Yes', 'No', 'No']
}
print("--- Initializing Data Cleaning Pipeline ---")
df = pd.DataFrame(raw_data)
# 1. Clean data formatting inconsistencies (remove spacing and symbols)
df['Monthly_Charges'] = df['Monthly_Charges'].str.replace('$', '').str.strip()
# 2. Handle missing structural numeric values
df['Monthly_Charges'] = pd.to_numeric(df['Monthly_Charges'], errors='coerce')
median_charge = df['Monthly_Charges'].median()
df['Monthly_Charges'] = df['Monthly_Charges'].fillna(median_charge)
# 3. Handle missing categorical labels safely
df['Contract_Type'] = df['Contract_Type'].fillna('Unknown')
# 4. Export clean production dataset layout
print("\n[SUCCESS] Pipeline Executed. Cleaned Data Summary:")
