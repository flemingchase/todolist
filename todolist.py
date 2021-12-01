from pathlib import Path
import manager

#set todolist path
todolist = Path.home().joinpath('.todolist')

def main():
    #create menu
    option = manager.menu()

    #while the option is not exit
    while option:
        manager.switcher(option, todolist)
        option = manager.menu()

if __name__ == "__main__":
    if not todolist.exists():
        todolist.touch()
    main()
