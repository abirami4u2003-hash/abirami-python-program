import matplotlib.pyplot as plt

# Runtime input
n = int(input("Enter number of months: "))

months = []
units = []

for i in range(n):
    month = input("Enter month name: ")
    unit = float(input("Enter electricity units: "))
    months.append(month)
    units.append(unit)

# Create dashboard
plt.figure(figsize=(12, 4))

# 1. Line Chart
plt.subplot(1, 3, 1)
plt.plot(months, units, marker="o", color="blue")
plt.title("Electricity Usage Trend")
plt.xlabel("Months")
plt.ylabel("Units")
plt.xticks(rotation=45)

# 2. Bar Chart
plt.subplot(1, 3, 2)
plt.bar(months, units, color="orange")
plt.title("Electricity Usage Comparison")
plt.xlabel("Months")
plt.ylabel("Units")
plt.xticks(rotation=45)

# 3. Pie Chart
plt.subplot(1, 3, 3)
plt.pie(units, labels=months, autopct="%1.1f%%")
plt.title("Electricity Usage Distribution")

plt.tight_layout()
plt.show()

