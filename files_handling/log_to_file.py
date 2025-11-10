
class LogFiles:
    def __init__(self, data):
        self.data = data
        self.users_file = None
        self.books_file = None
        self.create_users_file()
        self.create_books_file()

    def create_users_file(self):
        try:
            with open("users_list.json", "x") as users_file:
                self.users_file = "users_list.json"
        except FileExistsError:
            print(f"file{self.users_file} already exists")

    def create_books_file(self):
        try:
            with open("books_list.json", "x") as books_file:
                self.books_file = books_file
        except FileExistsError:
            print(f"file{self.books_file} already exists")

    def log_files(self):
        file_name = self.users_file
        with open("users_list.json", "a") as file:
            file.write(f"{self.data}\n")

