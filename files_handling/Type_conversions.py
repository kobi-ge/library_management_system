import json

class ConvertToPython:
    def __init__(self, data):
        self.data = data

    def json_to_python(self):
        python_data = json.loads(self.data)
        return python_data

    def get_data_from_dict(self):
        self.data = self.data["data"]
        return self.data

class ConvertToJson:
    def __init__(self, data):
        self.data = data
        self.type = type(data)

    def convert_to_dict(self):
        self.data = {"data": self.data ,"type": self.type}
        return self.data

    def python_to_json(self):
        json_data = json.dumps(self.data)
        return json_data
