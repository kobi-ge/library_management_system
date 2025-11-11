
class CreateFiles:
    def __init__(self, library_name):
        self.library_name = library_name
        self.name = ""
        self.file_type = ["books", "users"]

    def set_name(self, num):
        self.name = self.library_name + self.file_type[num] + ".json"
        return self.name

    def create_file(self):
        try:
            with open(self.name, "x") as file:
                pass
        except FileExistsError:
            print(f"file {self.name} already exists")

    def run_creation(self):
        for file_name in range(2):
            self.set_name(file_name)
            self.create_file()
