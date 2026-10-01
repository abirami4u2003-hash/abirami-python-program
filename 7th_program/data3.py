import pandas as pd
import numpy as np

data = {
    "Student": ["Arun", "Bala", "Chitra", "Deepak", "Priya"],
    "Maths": [85, 75, 90, 65, 95],
    "Science": [80, 70, 85, 60, 90]
}

df = pd.DataFrame(data)

# Calculate total marks
df["Total"] = df["Maths"] + df["Science"]

# Calculate average marks
df["Average"] = df["Total"] / 2

print("Student Data:")
print(df)

print("\nTotal Marks:", np.sum(df["Total"]))
print("Average Marks:", np.mean(df["Average"]))
print("Maximum Marks:", np.max(df["Total"]))
print("Minimum Marks:", np.min(df["Total"]))

print("\nStatistical Summary:")
print(df.describe())

print("\nTop Student:")
print(df.loc[df["Total"].idxmax()])
