while True:
    print("\n--- Student Grade Analyzer ---")
    print("1. Analyze Grades")
    print("2. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter number of subjects: "))
        total = 0

        for i in range(n):
            mark = float(input(f"Enter mark for subject {i + 1}: "))
            total += mark

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
            grade = "D"
        else:
            grade = "F"

        print("\nTotal Marks:", total)
        print("Average:", round(average, 2))
        print("Final Grade:", grade)

    elif choice == 2:
        print("Program ended.")
        break

    else:
        print("Invalid choice!")
