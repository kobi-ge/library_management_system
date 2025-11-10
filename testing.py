import json
#
# a = 234
# b = json.dumps(a)
# print(b)
# print(type(b))

# class A:
#     def __init__(self):
#         self.a = 2
#
# a = A()
# print(type(a) == A)



class ConvertToJson:
    def __init__(self, data):
        self.data = data
        self.type = type(data).__name__

    def convert_to_dict(self):
        self.data = {"data": self.data ,"type": self.type}
        return self.data

    def python_to_json(self):
        self.convert_to_dict()
        json_data = json.dumps(self.data)
        return json_data, self.type

a = ConvertToJson(123)
print(a.data)
b = a.python_to_json()
print(b)


# class ConvertToPython:
#     def __init__(self, data):
#         self.data = data
#
#     def json_to_python(self):
#         self.data = json.loads(self.data)
#         return self.data
#
#     def get_data_from_dict(self):
#         self.data = self.data["data"]
#         return self.data
#
# a = ConvertToPython(b)
# a.json_to_python()
# print((a.get_data_from_dict()))

#import files_handling.Type_conversions as t, files_handling.log_to_file as f

# a = t.ConvertToJson(1234)
# a.convert_to_dict()
# b= a.python_to_json()
#
# c = f.LogFiles(b)
# c.create_users_file()
# c.log_files()
#
#
# a2 = t.ConvertToJson(5678)
# a.convert_to_dict()
# b2 = a2.python_to_json()
#
# c2 = f.LogFiles(b2)
# c2.log_files()

