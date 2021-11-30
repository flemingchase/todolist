from pathlib import Path

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

#Gives options for todolist
def menu():
    return 0
