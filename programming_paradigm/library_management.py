class Book:
    def __init__(self, title ,author):
        self.title = title
        self.author = author
        self._is_checked_out = False
        
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        return not self._is_checked_out
    
    def __str__(self):
        status = "check out" if self._is_checked_out else "available"
        return f"{self.title} by {self.author} ({status})"
            


class Library:
    def __init__(self):
        self._books = []
        
    def add_book(self,book):
        if isinstance(book, Book):
            self._books.append(book)
            return True
        return False
    
    def check_out_book(self,title):
        for book in self._books:
            if book.title == title and book.is_available():
                return book.return_book()
        return False
    
    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                return book.return_book()
        return False
    
    def list_available_books(self):
        return self._books
