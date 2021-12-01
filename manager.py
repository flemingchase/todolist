from pathlib import Path

#Options for interactive menu
options = ['1: Add to todo list.',
            '2: Remove an item from todo list.',
            '3: Print your todo list.',
            '4: Clear list.',
            '0: Exit.']

#Adds item to todolist
def add_item(item, pathtolist):
    return 0

#Removes item number from todolist
def remove_item(number, pathtolist):
    return 0

#Prints todolist
def print_todolist(pathtolist):
    with pathtolist.open() as todolist:
        print(todolist.readline())

#Clears todolist
def clear_todolist(pathtolist):
    pathtolist.unlink()

#Gives options for todolist
def menu():
    for option in options:
        print(option)

    try:
        return int(input('Select an option: '))
    except ValueError:
        print('Please enter an integer.')
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
                pass
            remove_item(number, pathtolist)

        case 3:
            print_todolist(pathtolist)

        case 4:
            clear_todolist(pathtolist)

        case 0:
            return False

        case _:
            print('select another option')

