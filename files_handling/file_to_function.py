import json

class GetFileData:
    def __init__(self, file_name):
        self.data_list = []
        self.file_name = file_name

    def getting_data(self) -> list:
        with open(self.file_name, "r") as f:
            for line in f.readlines():
                data_dict = json.loads(line)
                self.data_list.append(data_dict["data"])
        return self.data_list
