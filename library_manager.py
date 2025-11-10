from cure.library import Library

class Manager:
    def __init__(self):
        self.library = Library()

    def analyze_choice(self,choice):

    def get_user_choice(self):
        correct_answer = ['1','2','3']
        while True:
            print("1. Add Book\n2. Add User\n3. Borrow Book\n7. Save & Exit")
            choice = input("Enter your choice: ")
            if choice in correct_answer:
                return choice
            else:
                print('try again')
