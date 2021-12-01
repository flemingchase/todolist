#!/usr/bin/env python

from pathlib import Path
import manager

#set todolist path
todolist = Path.home().joinpath('.todolist')

def main():
    #Print todolist
    manager.print_todolist(todolist)
    exit = True

    #Show interactive menu
    while exit:
        option = manager.menu()
        if not option == -1:
            exit = manager.switcher(option, todolist)
        else:
            pass


if __name__ == "__main__":
    if not todolist.exists():
        todolist.touch()
    main()
