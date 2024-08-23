class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_borrowed = False

    def borrow_book(self):
        if self.is_borrowed:
            print("Sorry, the book is already borrowed.")
        else:
            self.is_borrowed = True
            print("Book successfully borrowed.")

    def return_book(self):
        self.is_borrowed = False
        print("Book returned.")



class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def display_available_books(self):
        print("Available books in the library:")
        for book in self.books:
            if not book.is_borrowed:
                print(f"{book.title} by {book.author}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                book.borrow_book()
                return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.return_book()
                return
        print(f"Book '{title}' not found in the library.")


book1 = Book("Python Programming", "Guido van Rossum", 350)
book2 = Book("Machine Learning Basics", "Andrew Ng", 250)
book3 = Book("Data Structures and Algorithms", "John Smith", 400)

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display_available_books()

library.borrow_book("Python Programming")
library.borrow_book("Machine Learning Basics")

library.display_available_books()

library.return_book("Python Programming")

library.display_available_books()
