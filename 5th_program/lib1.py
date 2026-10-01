class Book:
    def __init__(self, title):
        self.title = title
        self.issued = False

    def issue(self):
        if not self.issued:
            self.issued = True
            print(self.title, "has been issued.")
        else:
            print(self.title, "is already issued.")

    def return_book(self):
        self.issued = False
        print(self.title, "has been returned.")


class User:
    def __init__(self, name):
        self.name = name

    def display_role(self):
        print("Library User:", self.name)


class Student(User):
    def display_role(self):
        print("Student:", self.name)


class Teacher(User):
    def display_role(self):
        print("Teacher:", self.name)


book = Book("Python Programming")

student = Student("Arun")
teacher = Teacher("Kumar")

student.display_role()
book.issue()

teacher.display_role()
book.return_book()
