class Book:
          def __init__(self, title : str, author: str):
                  assert isinstance(title, str), "Title must be a string"
                  self.title = title
                  self.author = author
          def __str__(self):
                  return f"{self.title} by {self.author}"      
class EBook(Book):
          def __init__(self, title : str, author: str, size: int):
                  super().__init__(title, author)
                  self.size = size
          

class PrintBook(Book):
          def __init__(self, title : str, author: str, page_count: int):
                  super().__init__(title, author)
                  self.page_count = page_count

"""""
Composition - Library:

Attributes: books (a list to store instances of Book, EBook, and PrintBook).
Methods:
add_book(self, book): Adds a Book, EBook, or PrintBook instance to the library.
list_books(self): Prints details of each book in the library.
"""""


class Library:
          def __init__(self):
                  self.books = []
          def add_book(self, book):
                  self.books.append(book)
          def list_books(self):
                  for book in self.books:
                          print(book.title, book.author)

"""""
Book: Pride and Prejudice by Jane Austen
EBook: Snow Crash by Neal Stephenson, File Size: 500KB
PrintBook: The Catcher in the Rye by J.D. Salinger, Page Count: 234
"""""