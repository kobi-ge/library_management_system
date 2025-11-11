

class Library:
    def __init__(self,name_library):
        self.name_library = name_library
        self.users_list = []
        self.book_list = []

    def add_book(self,book):
        # remove we need adding to the file
        self.book_list.append(book)

    def add_user(self,user):
        self.users_list.append(user)

    def user_in_library(self, user_id):
        for user in self.users_list:
            if user.get_id() == user_id:
                return True
        else:
            return False

    def book_in_library(self, book_title):
        for book in self.book_list:
            if book.get_book_title() == book_title:
                return book
        else:
            return None

    def borrow_book(self, user_id, book_title):
        if self.user_in_library(user_id):
            book = self.book_in_library(book_title)
            if book :
                if book.book_loan():
                    self.users_list.append(book)
                else:
                    print('book not available')
            else:
                print('book not found')
        else:
            print('user not exits')

    def return_book(self, user_id, book_isbn):
        if self.user_in_library(user_id):
            for book in self.book_list:
                if book.get_isbn_book() == book_isbn:
                    if book.book_returning():
                        self.users_list.remove(book)
                    else:
                        print('Already returned')
            else:
                print('book is not exist')
        else:
            print('user not exist')


    def list_available_books(self):
        return [book for book in self.book_list if book.is_available]

    def search_book_by_title(self, title):
        for book in self.book_list:
            if book.get_book_title() == title:
                print('book found')
                print(book)
                return book
        else:
            print('book not exist')
            return None

    def search_by_author(self,author):
        for book in self.book_list:
            if book.get_book_author() == author:
                print('book found')
                print(book)
                return book
        else:
            print('book not exist')
            return None

