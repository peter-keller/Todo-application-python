import sys


def add_todo(todo_text):
    todo_list = create_dictonary()
    if todo_list != []:
        todo_list[-1]["todo"] = todo_list[-1]["todo"][0:] + "\n"
    todo_dict = {}
    todo_dict["complete"] = False
    todo_dict["todo"] = todo_text
    todo_list.append(todo_dict)
    save_to_file(todo_list)

def remove_todo(number):
    todo_list = create_dictonary()
    if number <= len(todo_list) and number > 0:
        del todo_list[number-1]
    else:
        print("The number is out of range!")
    save_to_file(todo_list)

def save_to_file(todo_list_updated):
    try:
        server_text = ""
        for dict_item in todo_list_updated:
            if dict_item["complete"]:
                server_text += "1 "
            else:
                server_text += "0 "
            server_text += dict_item["todo"]
        fw = open("todo_list.txt", "w")
        fw.write(server_text)
        fw.close()
    except IOError:
        print("Unable to write file: files/decrypt-lines.txt")


def intro():
    text = "\nCommand Line Todo Application\n"
    text += "=============================\n\n"
    text += "Command line arguments:\n"
    text += "-l   Lists all the tasks\n"
    text += "-a   Adds a new task\n"
    text += "-r   Removes an task\n"
    text += "-c   Completes an task\n\n"
    text += "Please choose a selector!"
    return text

def command_selector():
    if sys.argv[-1] == 'todo.py':
        print(intro())
    elif sys.argv[-1] == '-l':
        print_list()
    elif sys.argv[-1] == '-c':
        print("Please add your todos number after c!")
    elif sys.argv[-1] == '-u':
        print("Please add your todos number after u!")
    elif sys.argv[-1] == '-a':
        print("Please add your todo after a!")
    elif sys.argv[-1] == '-r':
        print("Please add your todos number after r!")
    elif sys.argv[-2] == '-c':
        make_complete(int(sys.argv[-1]))
    elif sys.argv[-2] == '-u':
        make_uncomplete(int(sys.argv[-1]))
    elif sys.argv[-2] == '-a':
        add_todo(sys.argv[-1])
    elif sys.argv[-2] == '-r':
        remove_todo(int(sys.argv[-1]))
    else:
        print("Undefined selector")

def make_complete(number):
    todo_list = create_dictonary()
    if number <= len(todo_list) and number > 0:
        todo_list[number-1]["complete"] = True
    else:
        print("The number is out of range!")
    save_to_file(todo_list)

def make_uncomplete(number):
    todo_list = create_dictonary()
    if number <= len(todo_list) and number > 0:
        todo_list[number-1]["complete"] = False
    else:
        print("The number is out of range!")
    save_to_file(todo_list)

def create_dictonary():
    try:  
        todo_list = []
        fr = open('todo_list.txt', "r")
        lines_list = fr.readlines()
        for line in lines_list:
            todo_dict = {}
            if line[0] == "0":
                todo_dict["complete"] = False
            else:
                todo_dict["complete"] = True
            todo_dict["todo"] = line[2:]
            todo_list.append(todo_dict)
        return todo_list
        fr.close()
    except IOError:
        print("Unable to read file: todo_list.txt")


def print_list():
    user_text = ""
    todo_list = create_dictonary()
    if todo_list == []:
        print("No todos for today! :)")
    else:
        i = 1
        for dict_item in todo_list:
            user_text += str(i) + " - "
            if dict_item["complete"]:
                user_text += "[x] "
            else:
                user_text += "[ ] "
            user_text += dict_item["todo"]
            i += 1
        print(user_text)
    

def main():
    command_selector()

main()