import json
from files_handling.log_to_file import LogFiles

class ConvertToPython:
    def __init__(self, data):
        self.data = data

    def json_to_python(self):
        self.data = json.loads(self.data)
        return self.data

class GetData:
    def __init__(self, data):
        self.data = data

    def get_data_from_dict(self):
        self.data = self.data["data"]
        return self.data



class ConvertToDict:
    def __init__(self, data):
        self.data = data
        self.type = type(self.data).__name__

    def conversion(self):
        self.data = {"data": self.data ,"type": self.type}
        return self.data

class DictToJson:
    def __init__(self, data):
        self.data = data
        self.type = type(self.data["data"]).__name__

    def conversion(self):
        json_data = json.dumps(self.data)
        return json_data, self.type

