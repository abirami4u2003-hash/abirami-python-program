class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def issue(self, user):
        if self.available:
            self.available = False
            print(self.title, "issued to", user.name)
        else:
            print("Book is unavailable.")

    def return_book(self):
        self.available = True
        print(self.title, "has been returned.")

    def display(self):
        status = "Available" if self.available else "Issued"
        print(self.title, "-", self.author, "-", status)


class User:
    def __init__(self, name):
        self.name = name

    def borrow_limit(self):
        return 1


class Student(User):
    def borrow_limit(self):
        return 3


class Faculty(User):
    def borrow_limit(self):
        return 5


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            book.display()


library = Library()

book1 = Book("Python Programming", "John")
book2 = Book("Data Structures", "James")
book3 = Book("Database Systems", "Robert")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

student = Student("Karthik")
faculty = Faculty("Priya")

print("Student borrowing limit:", student.borrow_limit())
print("Faculty borrowing limit:", faculty.borrow_limit())

print("\n--- Available Books ---")
library.show_books()

print("\n--- Issue Book ---")
book1.issue(student)

print("\n--- Books After Issue ---")
library.show_books()

print("\n--- Return Book ---")
book1.return_book()

print("\n--- Books After Return ---")
library.show_books()
