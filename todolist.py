#!/usr/bin/env python3

from pathlib import Path
import manager

#set todolist path
todolist = Path.home().joinpath('.todolist')

def main():
    manager.print_todolist(todolist)
    while True:
        manager.menu()
        try:
            option = int(input('Select an option: '))
        except ValueError:
            print('Please enter an integer.')
            pass
        print(option)

if __name__ == "__main__":
    if not todolist.exists():
        todolist.touch()
    main()
