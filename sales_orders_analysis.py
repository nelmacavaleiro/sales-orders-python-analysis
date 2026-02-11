# ==========================================
# Sales Orders Analysis - Python Fundamentals
# Author: Nelma Cavaleiro
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------
# 1. Load the CSV file
# ------------------------------------------

file_path = r"C:\Users\nelma\OneDrive\Documents\Portfolio\sales-orders-python-analysis\Sales_Orders_Clean.csv"
df = pd.read_csv(file_path)

print("Dataset loaded successfully")

# ------------------------------------------
# 2. Data inspection
# ------------------------------------------

print("\nShape (rows, columns):")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("\nMissing values per column:")
print(df.isnull().sum())

# ------------------------------------------
# 3. Ensure correct data types
# ------------------------------------------

# Clean Sales column (remove $ if present)
df["Sales"] = df["Sales"].astype(str).str.replace("$", "").str.replace(",", "")
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")

# Clean Item Cost column (remove $ if present)
df["Item Cost"] = df["Item Cost"].astype(str).str.replace("$", "").str.replace(",", "")
df["Item Cost"] = pd.to_numeric(df["Item Cost"], errors="coerce")

# Clean Unit Sold column
df["Unit Sold"] = pd.to_numeric(df["Unit Sold"], errors="coerce")

# Calculate Profit
df["Profit"] = df["Sales"] - df["Item Cost"]

# Calculate Profit Margin
df["Profit_Margin"] = (df["Profit"] / df["Sales"] * 100).round(2)

print("\nData types after conversion:")
print(df[["Sales", "Profit", "Unit Sold"]].dtypes)

# ------------------------------------------
# 4. Overall metrics
# ------------------------------------------

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
average_sales = df["Sales"].mean()
max_sales = df["Sales"].max()

print("\n--- Overall Metrics ---")
print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))
print("Average Sales:", round(average_sales, 2))
print("Maximum Sale:", round(max_sales, 2))

# ------------------------------------------
# 5. Sales by Year
# ------------------------------------------

sales_by_year = (
    df.groupby("Year")["Sales"]
    .sum()
    .reset_index()
    .sort_values("Year")
)

print("\nSales by Year:")
print(sales_by_year)

# ------------------------------------------
# 6. Profit by Region
# ------------------------------------------

profit_by_region = (
    df.groupby("Region")["Profit"]
    .sum()
    .reset_index()
    .sort_values("Profit", ascending=False)
)

print("\nProfit by Region:")
print(profit_by_region)

# ------------------------------------------
# 7. Average Profit Margin by Segment
# ------------------------------------------

profit_margin_by_segment = (
    df.groupby("Segment")["Profit_Margin"]
    .mean()
    .reset_index()
    .sort_values("Profit_Margin", ascending=False)
)

print("\nAverage Profit Margin by Segment:")
print(profit_margin_by_segment)

# ------------------------------------------
# 8. Visualisations
# ------------------------------------------

# Sales by Year
plt.figure(figsize=(10, 6))
plt.plot(sales_by_year["Year"], sales_by_year["Sales"], marker="o", linewidth=2)
plt.title("Total Sales by Year")
plt.xlabel("Year")
plt.ylabel("Sales ($)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Profit by Region
plt.figure(figsize=(10, 6))
plt.bar(profit_by_region["Region"], profit_by_region["Profit"], color="steelblue")
plt.title("Total Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit ($)")
plt.tight_layout()
plt.show()

# ------------------------------------------
# 9. End of analysis
# ------------------------------------------

print("\nAnalysis completed successfully.")
