
class LogFiles:
    def __init__(self, data, name):
        self.data = data
        self.file_name = name

    def log_files(self):
        with open(self.file_name, "a") as file:
            file.write(f"{self.data}\n")

