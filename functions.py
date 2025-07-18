FILEPATH = 'todos.txt'

def get_todos(file_path = FILEPATH):
    """this is a doc strings"""
    with open(file_path, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_list, file_path = FILEPATH):
    with open(file_path, 'w') as file_local:
        file_local.writelines(todos_list)

# print(__name__)
# this will only run when this file is executed not on the cli.py
if __name__  == "__main__":
    print("Hello")