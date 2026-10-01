n = int(input("Enter number of subjects: "))
marks = []

for i in range(n):
    mark = float(input(f"Enter mark {i + 1}: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("\nMarks:", marks)
print("Total:", total)
print("Average:", round(average, 2))
print("Grade:", grade)
