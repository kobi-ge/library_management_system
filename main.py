from library_manager import Manager
def get_name_library():
    while True:
        library = input('enter library name')
        if library.isalpha():
            return library
def main():
    library = Manager(get_name_library())
    library.run_manager()

if __name__ == '__main__':
    main()