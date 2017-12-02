import sys

todo_file = "todo_list.txt"



def open_file():
    try:
        with open(todo_file, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(todo_file + " not found")


def save_to_file(argument):
    try:
        with open(todo_file, 'w') as file:
            return file.write()
    except FileNotFoundError:
        print(todo_file + " not found")


def add():
    pass


def remove():
    pass


def complete():
    pass

