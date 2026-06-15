# 📞 Telecom Customer Churn Data Cleaning & EDA (Python)
## 🎯 Business Problem
The retention team is experiencing high subscriber turnover (churn) but cannot trust their historical customer records due to inconsistent formatting, missing transaction variables, and extreme data noise.
## 🛠️ Data Strategy & Pipeline
Using Python (`Pandas` and `NumPy`), I engineered a data cleaning script to prepare the pipeline for analytical modeling:
1. **Structural Auditing:** Standardized messy column headers and structural datatypes.
2. **Handling Anomalies:** Imputed missing billing inputs using local median benchmarks.
3. **Feature Engineering:** Converted raw usage text fields into standardized binary behavioral metrics.
## 📈 Key Discovery
Customers on month-to-month contracts who call customer service more than 3 times have a **72% higher probability of leaving** within 30 days compared to long-term contract users.
