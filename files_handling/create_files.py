
class CreateFile:
    def __init__(self, library_name, file_type):
        self.library_name = library_name
        self.file_type = file_type
        self.name = ""

    def set_name(self):
        self.name = self.library_name + self.file_type + ".json"
        return self.name

    def create_users_file(self):
        try:
            with open(self.name, "x") as file:
                pass
        except FileExistsError:
            print(f"file {self.name} already exists")
