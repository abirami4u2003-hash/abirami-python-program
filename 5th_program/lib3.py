class Book:
    def __init__(self, title):
        self.title = title
        self.available = True

    def issue(self):
        if self.available:
            self.available = False
            print("Book issued:", self.title)
        else:
            print("Book already issued.")

    def return_book(self):
        if not self.available:
            self.available = True
            print("Book returned:", self.title)
        else:
            print("Book was not issued.")


class User:
    def __init__(self, name):
        self.name = name

    def user_type(self):
        return "User"


class Student(User):
    def user_type(self):
        return "Student"


class Teacher(User):
    def user_type(self):
        return "Teacher"


book = Book("Computer Networks")
student = Student("Anjali")

while True:
    print("\n--- LIBRARY MENU ---")
    print("1. Display User")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Name:", student.name)
        print("Type:", student.user_type())

    elif choice == "2":
        book.issue()

    elif choice == "3":
        book.return_book()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
