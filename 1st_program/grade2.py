# Student Grade Analyzer using while loop

n = int(input("Enter number of subjects: "))

total = 0
count = 1

while count <= n:
    mark = float(input(f"Enter mark for subject {count}: "))
    total += mark
    count += 1

average = total / n

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    puth
    grade = "D"
else:
    grade = "F"

print("\nTotal Marks =", total)
print("Average =", average)
print("Grade =", grade)
