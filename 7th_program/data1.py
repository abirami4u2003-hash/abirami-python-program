import pandas as pd
import numpy as np

data = {
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone"],
    "Sales": [50000, 30000, 20000, 45000, 35000],
    "Quantity": [2, 3, 4, 1, 5]
}

df = pd.DataFrame(data)

# Calculate total revenue
df["Revenue"] = df["Sales"] * df["Quantity"]

print("Sales Data:")
print(df)

print("\nTotal Revenue:", np.sum(df["Revenue"]))
print("Average Revenue:", np.mean(df["Revenue"]))
print("Maximum Revenue:", np.max(df["Revenue"]))
print("Minimum Revenue:", np.min(df["Revenue"]))

print("\nStatistical Summary:")
print(df.describe())

print("\nHighest Revenue Product:")
print(df.loc[df["Revenue"].idxmax()])
