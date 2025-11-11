from cure.library import Library
from cure.book import Book
from cure.isbn import Isbn
from cure.user import User


class Manager:
    correct_answer = ['1','2','3','4','7']

    def __init__(self,name_library):
        self.library = Library(name_library)
        self.server_on = True

    def get_user_choice(self):
        while True:
            print("1. Add Book\n2. Add User\n3. Borrow Book\n4. Returning book\n7. Save & Exit")
            choice = input("Enter your choice: ")
            if choice in self.correct_answer:
                return choice
            else:
                print('try again')

    def analyze_choice(self,choice):
        if choice == '1':
            book_info = get_book_info()
            isbn = Isbn()
            new_book = Book(book_info[0],book_info[1],isbn)

            self.library.add_book(new_book)

        elif choice == '2':
            user_info = get_user_info()
            new_user = User(user_info[0], user_info[1])

            self.library.add_user(new_user)

        elif choice == '3':
            # tuple name and id
            user_info = get_user_info()
            if self.login(user_info[1]):
            # book name
                book_info = get_book_info()
                self.library.borrow_book(user_info[1], book_info)
            else:
                print('you are not user.')

        elif choice == '4':
            user_info = get_user_info()
            if self.login(user_info[1]):
                book_info = get_book_info()
                self.library.return_book(user_info[1], book_info)

        elif choice == '7':
            self.server_on = False
    #         saving data

    def run_manager(self):
        print(f'welcome to {self.library.name_library} library')

        while self.server_on:
            choice = self.get_user_choice()
            self.analyze_choice(choice)

    def login(self,user_id):
        if self.library.user_in_library(user_id):
            return True
        else:
            return False




def get_user_info():
    while True:
        name = input('enter your name')
        if name.isalpha():
            user_id = input('enter your id')
            if  user_id.isdigit():
                return name , int(user_id)
            else:
                print('not valid id')
        else:
            print('not valid name')


def get_book_info():
    # option for addition search by auther
    while True:
        print('for adding book \nenter book information')
        title = input('enter title')
        if title.isalpha():
            author = input('enter author')
            if  author.isalpha():
                return title
            else:
                print('not valid author')
        else:
            print('not valid title')

