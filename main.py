from add import add
from update import update
from delete import delete
from list_tasks import list_all, list_done, list_in_progress, list_todo
from progress_manager import mark_done, mark_in_progress
import argparse

parser = argparse.ArgumentParser(
                    prog='Task-Tracker',
                    description='With task-tracker you can manage and track your tasks',
                    epilog='this was a fun little project')
parser.add_argument("command")
parser.add_argument("arg1", nargs="?")
parser.add_argument("arg2", nargs="?")
args = parser.parse_args()
command = args.command
arg1 = args.arg1
arg2 = args.arg2

def main():
    match command:
        case "add":
            add(arg1)
        case "delete":
            delete(arg1)
        case "update":
            try:
                update(arg1, arg2)
            except Exception as e:
                print(e)
        case "list":
            if not arg1:
                list_all()
            elif arg1 == "done":
                list_done()
            elif arg1 == "todo":
                list_todo()
            elif arg1 == "in-progress":
                list_in_progress()
            else:
                 print(arg1, "is not a valid command")
        case "mark-done":
            mark_done(arg1)
        case "mark-in-progress":
            mark_in_progress(arg1)
        case "help":
            print("add, delete, update, list -all, list -not, list-inp, help, stop")
        case _:
            print(command, "is not a valid command")
            print('use "help" command to see all commands')


if __name__=="__main__":
    main()