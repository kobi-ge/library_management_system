

class Book:

    def __init__(self,title:str,author:str,isbn):
        self._title = title
        self._author = author
        self._isbn = isbn
        self.is_available = True

    def get_book_title(self):
        return self._title

    def get_isbn_book(self):
        return self._isbn

    def get_book_author(self):
        return self._author

    def book_loan(self):
        if self.is_available:
            self.is_available = False
            return True
        else:
            return False

    def book_returning(self):
        if not self.is_available:
            self.is_available = True
            return True
        else:
            return False

    def __str__(self):
        return f'title:{self._title}\nauthor:{self._author}\nISBN:{self._isbn}'
