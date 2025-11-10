

class User:

    def __init__(self, name:str, user_id:int):
        self. name = name
        self.user_id = user_id
        self.borrowed_books = []

    def add_book(self,book):
        self.borrowed_books.append(book)

    def get_id(self):
        return self.user_id

    def show_count(self):
        for book in self.borrowed_books:
            print(book.get_book_title())
