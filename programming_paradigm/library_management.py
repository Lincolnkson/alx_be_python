class Book:
    """
    Represents a book in the library with title, author, and checkout status.
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def check_out(self):
        """Marks the book as checked out if it's available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        """Marks the book as returned if it was checked out."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        """Returns whether the book is available for checkout."""
        return not self._is_checked_out
    
    def __str__(self):
        """Returns a string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """
    Manages a collection of books and their availability status.
    """
    def __init__(self):
        self._books = []
    
    def add_book(self, book):
        """Adds a new book to the library."""
        self._books.append(book)
    
    def check_out_book(self, title):
        """
        Attempts to check out a book by title.
        Returns True if successful, False if book not found or already checked out.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                return book.check_out()
        return False
    
    def return_book(self, title):
        """
        Attempts to return a book by title.
        Returns True if successful, False if book not found or not checked out.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                return book.return_book()
        return False
    
    def list_available_books(self):
        """Prints all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(str(book))
        else:
            print("No books available.")