import json
from files_handling.log_to_file import LogFiles


class ConvertToDict:
    def __init__(self, data):
        self.data = data

    def conversion(self):
        self.data = {"data": self.data}
        return self.data

class DictToJson:
    def __init__(self, data):
        self.data = data

    def conversion(self):
        json_data = json.dumps(self.data)
        return json_data


