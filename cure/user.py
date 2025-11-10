

class User:

    def __init__(self, name:str, user_id:int):
        self._name = name
        self._user_id = user_id
        self.borrowed_books = []

    def add_book(self,book):
        self.borrowed_books.append(book)

    def remove_book(self,book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

    def get_user_name(self):
        return self._name

    def get_id(self):
        return self._user_id

    def show_books(self):
        for book in self.borrowed_books:
            print(book.get_book_title())
