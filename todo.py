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


def list_tasks():
    try:
        with open(todo_file, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(todo_file + " not found")


print(list_tasks())


def add():
    print("something")


def remove():
    pass


def complete():
    pass

def run():
    try:
        controller(add)()
    except KeyboardInterrupt:
        pass

def controller(task_name):
    return {
        "-a": add,
        "-r": remove,
        "-c": complete,
        "-l": list_tasks
    }[task_name]