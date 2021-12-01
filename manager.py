from pathlib import Path
import datetime as dt

#Options for interactive menu
options = ['1: Add to todo list.',
            '2: Remove an item from todo list.',
            '3: Print your todo list.',
            '4: Clear list.',
            '0: Exit.']

#Adds item to todolist
def add_item(item, pathtolist):
    with pathtolist.open('a+') as todolist:
        item = item.strip()
        todolist.write(item + '\n')

#Removes item number from todolist
def remove_item(number, pathtolist):
    with pathtolist.open('r+') as todolist:
        lines = todolist.readlines()
    try:
        del lines[number - 1]
    except IndexError:
        print('Select a valid entry.')
        return

    with pathtolist.open('w+') as todolist:
        for line in lines:
            todolist.write(line)

#Prints todolist
def print_todolist(pathtolist):
    print('*'*68)
    print('Printing todo list:')
    num = 1
    with pathtolist.open() as todolist:
        lines = todolist.readlines()
        for line in lines:
            print(str(num) + '. ' + line.strip())
            num += 1
    print('*'*68)

#Clears todolist
def clear_todolist(pathtolist, missing_ok=True):
    with pathtolist.open('r+') as todolist:
        todolist.truncate(0)
    print('*'*10)

#Gives options for todolist
def menu():
    for option in options:
        print(option)

    selection = input('Select an option: ')
    if selection:
        try:
            return int(selection)
        except ValueError:
            pass
    return -1


#Switcher for options
def switcher(option, pathtolist):
    match option:
        case 1:
            item = input('Item to add: ')
            add_item(item, pathtolist)

        case 2:
            try:
                number = int(input('Number of item to remove: '))
            except ValueError:
                print('Please input an integer.')
            remove_item(number, pathtolist)

        case 3:
            print_todolist(pathtolist)

        case 4:
            clear_todolist(pathtolist)

        case _:
            print('Select a valid option.')
