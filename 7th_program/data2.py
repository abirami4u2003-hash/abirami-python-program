import pandas as pd
import numpy as np

data = {
    "Employee": ["Arun", "Bala", "Chitra", "Deepak", "Priya"],
    "Salary": [30000, 45000, 50000, 35000, 60000],
    "Bonus": [3000, 5000, 6000, 3500, 7000]
}

df = pd.DataFrame(data)

# Calculate total income
df["Total Income"] = df["Salary"] + df["Bonus"]

print("Employee Data:")
print(df)

print("\nTotal Income:", np.sum(df["Total Income"]))
print("Average Income:", np.mean(df["Total Income"]))
print("Maximum Income:", np.max(df["Total Income"]))
print("Minimum Income:", np.min(df["Total Income"]))

print("\nStatistical Summary:")
print(df.describe())

print("\nHighest Paid Employee:")
print(df.loc[df["Total Income"].idxmax()])
