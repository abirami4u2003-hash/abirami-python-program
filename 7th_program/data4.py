import pandas as pd
import numpy as np

data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Printer", "Keyboard"],
    "Price": [50000, 30000, 20000, 15000, 2000],
    "Quantity": [5, 10, 8, 6, 20]
}

df = pd.DataFrame(data)

# Calculate total sales
df["Total Sales"] = df["Price"] * df["Quantity"]

print("Product Sales Data:")
print(df)

print("\nTotal Sales:", np.sum(df["Total Sales"]))
print("Average Sales:", np.mean(df["Total Sales"]))
print("Maximum Sales:", np.max(df["Total Sales"]))
print("Minimum Sales:", np.min(df["Total Sales"]))

print("\nStatistical Summary:")
print(df.describe())

print("\nHighest Selling Product:")
print(df.loc[df["Total Sales"].idxmax()])
