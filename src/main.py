from tasks_manager import *

data = load_tasks()

while True:
    print("\n--- Study Planner ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task complete")
    print("4. Delete task")
    print("5. Exit")

    choice = int(input("Choose an option:\t"))
    if choice == 1:
        add_task(data)
    elif choice == 2:
        view_task(data)
    elif choice == 3:
        mark_complete(data)
    elif choice == 4:
        del_task(data)
    elif choice == 5:
        break
    else:
        print("Invalid option, try again")
        