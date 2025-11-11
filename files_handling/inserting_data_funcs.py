
class InsertData:
    def __init__(self, new_data, old_dict):
        self.new_data = new_data
        self.dict = old_dict

    def insert(self):
        if self.new_data.isbn:
            self.dict["isbn"] = self.new_data
        else:
            self.dict["user_id"] = self.new_data

