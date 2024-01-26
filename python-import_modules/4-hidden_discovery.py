#!/usr/bin/python3
import marshal

def print_names_from_pyc(pyc_file):
    with open(pyc_file, 'rb') as file:
        file.read(8)
        
        code_object = marshal.load(file)
        names = [name for name in dir(code_object) if not name.startswith('__')]

        for name in sorted(names):
            print(name)

if __name__ == "__main__":
    pyc_file_path = 'hidden_4.pyc'
    print_names_from_pyc(pyc_file_path)
