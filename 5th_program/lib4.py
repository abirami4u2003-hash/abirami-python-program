class Book:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.issued_to = None

    def issue(self, user):
        if self.issued_to is None:
            self.issued_to = user
            print(self.title, "issued to", user.name)
        else:
            print("Book is already issued.")

    def return_book(self):
        if self.issued_to:
            print(self.title, "returned by", self.issued_to.name)
            self.issued_to = None
        else:
            print("Book is already available.")


class User:
    def __init__(self, name):
        self.name = name

    def borrow_book(self):
        print(self.name, "can borrow books.")


class Student(User):
    def borrow_book(self):
        print("Student", self.name, "can borrow up to 3 books.")


class Librarian(User):
    def borrow_book(self):
        print("Librarian", self.name, "can manage all books.")


book1 = Book(101, "Python")
book2 = Book(102, "Java")

student = Student("Ravi")
librarian = Librarian("Meena")

student.borrow_book()
librarian.borrow_book()

book1.issue(student)
book2.issue(student)

book1.return_book()
