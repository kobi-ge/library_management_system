from files_handling import file_to_function as ftf
from files_handling import log_to_file as ltf
from files_handling import type_conversion as tc

def main():
    #file_type = "Book"
    init_dict = tc.ConvertToDict(1234)
    data_dict = tc.ConvertToDict.conversion(init_dict)
    init_json = tc.DictToJson(data_dict)
    data_json = tc.DictToJson.conversion(init_json)
    print(data_json)

if __name__ == "__main__":
    main()

