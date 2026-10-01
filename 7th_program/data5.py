import pandas as pd
import numpy as np

data = {
    "Month": ["January", "February", "March", "April", "May"],
    "Units": [250, 300, 280, 350, 400],
    "Rate": [6, 6, 6, 6, 6]
}

df = pd.DataFrame(data)

# Calculate electricity bill
df["Bill"] = df["Units"] * df["Rate"]

print("Electricity Consumption Data:")
print(df)

print("\nTotal Units:", np.sum(df["Units"]))
print("Average Units:", np.mean(df["Units"]))
print("Maximum Units:", np.max(df["Units"]))
print("Minimum Units:", np.min(df["Units"]))

print("\nTotal Bill:", np.sum(df["Bill"]))
print("Average Bill:", np.mean(df["Bill"]))

print("\nStatistical Summary:")
print(df.describe())

print("\nHighest Consumption Month:")
print(df.loc[df["Units"].idxmax()])
