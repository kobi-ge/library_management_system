from cure.library import Library
from cure.book import Book
from cure.isbn import Isbn
from cure.user import User

class Manager:
    correct_answer = ['1', '2', '7']

    def __init__(self):
        self.library = Library()
        self.server_on = True
    def analyze_choice(self,choice):
        if choice == '1':
            book_info = self.get_book_info()
            isbn = Isbn()
            new_book = Book(book_info[0],book_info[1],isbn)

            self.library.add_book(new_book)

        elif choice == '2':
            user_info = self.get_user_info()
            new_user = User(user_info[0],user_info[1])

            self.library.add_user(new_user)

        elif choice == '7':
            self.server_on = False
    #         saving data

    def run_manager(self):

        while self.server_on:
            choice = self.get_user_choice()
            self.analyze_choice(choice)


    def get_user_info(self):
        while True:
            print('wellcome new member')
            name = input('enter your name')
            if not name.isalpha():
                print('not valid name')
                continue
            user_id = input('enter your id')
            if not user_id.isdigit():
                print('not valid id')
                continue
            return name , int(user_id)

    def get_book_info(self):
        while True:
            print('for adding book \nenter book information')
            title = input('enter title')
            if not title.isalpha():
                continue
            author = input('enter author')
            if not author.isalpha():
                continue
            return title,author

    def get_user_choice(self):
        while True:
            print("1. Add Book\n2. Add User\n3. Borrow Book\n7. Save & Exit")
            choice = input("Enter your choice: ")
            if choice in self.correct_answer:
                return choice
            else:
                print('try again')
