import json

class GetFileData:
    def __init__(self, file_name):
        self.data = None
        self.file_name = file_name

    def getting_data(self) -> str:
        with open(self.file_name, "r") as f:
            self.data = f.read()
        return self.data

    def extract_from_json(self):
        self.data = json.loads(self.data)
        return self.data
