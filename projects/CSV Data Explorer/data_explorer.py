# data_explorer.py

import pandas as pd

# Load CSV
df = pd.read_csv("data.csv")

# Show basic info
print("First 5 rows:")
print(df.head())

print("\nSummary statistics:")
print(df.describe())

print("\nNames of all people:")
print(df["Name"].tolist())

# Optional: average score
avg_score = df["Score"].mean()
print(f"\nAverage score: {avg_score}")
