class Book:
    def __init__(self, name):
        self.name = name
        self.available = True

    def issue(self):
        if self.available:
            self.available = False
            print(self.name, "issued successfully.")
        else:
            print(self.name, "is not available.")

    def return_book(self):
        self.available = True
        print(self.name, "returned successfully.")


class User:
    def __init__(self, name):
        self.name = name

    def get_limit(self):
        return 0


class Student(User):
    def get_limit(self):
        return 3


class Faculty(User):
    def get_limit(self):
        return 5


def show_limit(user):
    print(user.name, "can issue", user.get_limit(), "books.")


book = Book("Data Structures")

student = Student("Rahul")
faculty = Faculty("Priya")

show_limit(student)
show_limit(faculty)

book.issue()
book.return_book()
