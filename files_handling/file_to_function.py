
class GetFileData:
    def __init__(self):
        self.data_list = []

    def getting_data(self) -> list:
        with open("users_list.json", "r") as f:
            for line in f.readlines():
                self.data_list.append(line)
        return self.data_list

