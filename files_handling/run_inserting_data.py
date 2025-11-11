import reading_file, log_to_file, type_conversion, inserting_data_funcs, create_files


current_list = "books_list"
def run_update(new_data, file_name):
    old_dict = {}
    if current_list:
        file = reading_file.GetFileData("lib1books.json")
        file.getting_data()
        old_dict = file.extract_from_json()
    updated_dict = inserting_data_funcs.InsertData(new_data, old_dict).insert()
    json_data = type_conversion.DictToJson(updated_dict)
    log_to_file.LogFiles(json_data, file_name)







            # file = reading_file.GetFileData("lib1books.json")
            # file.getting_data()
            # data = file.extract_from_json()
            # print(data)

            # file = GetFileData("data.json")  # צור אובייקט
            # file.getting_data()  # קרא את תוכן הקובץ (מכניס למשתנה self.data)
            # data = file.extract_from_json()

