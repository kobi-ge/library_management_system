
class LogFiles:
    def __init__(self, data, file_name):
        self.data = data
        self.file_name = file_name

    def log_files(self):
        with open(self.file_name, "a") as file:
            file.write(self.data)


