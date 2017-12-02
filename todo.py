import sys

todo_file = "todo_list.txt"



def open_file():
    try:
        with open(todo_file, 'r') as file:
            return file.read
    except FileNotFoundError:
        print(todo_file + " not found")


def save_to_file():
    pass


def print_data():
    pass


def add():
    pass


def remove():
    pass


def complete():
    pass
