import json

class GetFileData:
    def __init__(self):
        self.data_list = []

    def getting_data(self) -> list:
        with open("users_list.json", "r") as f, open("books_list.json", ):
            for line in f.readlines():
                data_dict = json.loads(line)
                self.data_list.append(data_dict["data"])
        return self.data_list

