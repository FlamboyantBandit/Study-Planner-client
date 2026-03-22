import json
import os

FILE = "planner.json"

def load_tasks():
    if not os.path.exists(FILE):
        return {"tasks":[]}
    with open(FILE, 'r') as file:
        return json.load(file)
    
def save_tasks(data):
    with open(FILE, 'w') as file:
        json.dump(data, file, indent=2)

def add_task(data):
    sub = input("Subject:\t")
    topic = input("Topic:\t")
    assign = input("Assigning Date (DD-MM-YYYY):\t")
    due = input("Due Date (DD-MM-YYYY):\t")
    priority = int(input("Priority (1-10):\t"))

    task = {
        "id": max((task["id"] for task in data["tasks"]), default=0) + 1,
        "subject": sub,
        "topic": topic,
        "assign_date": assign,
        "due_date": due,
        "priority": priority,
        "status": "Pending",
        "complete_date": ""
    }

    data["tasks"].append(task)
    save_tasks(data)
    print("Task has been added\n")

def view_task(data, tasks):
    tasks = tasks if tasks is not None else data["tasks"]

    if not data["tasks"]:
        print("No tasks added yet")
        return
    for task in tasks:
        print(f"\n[{task["id"]}] {task["subject"]} - {task["topic"]}")
        print(f"Due: {task["due_date"]} | Priority: {task["priority"]} | Status: {task["status"]}")

def mark_complete(data):
    view_task(data)
    task_id = int(input("\nEnter task ID to mark its completion:\t"))
    for task in data["tasks"]:
        if task["id"] == task_id:
            task["status"] = "Completed"
            inp = input("Date of Completion (DD-MM-YYYY):\t")
            task["complete_date"] = inp
            save_tasks(data)
            print(str(task_id) + " Marked Complete")
            return            
    print("Task not found")

def del_task(data):
    view_task(data)
    task_id = int(input("\nEnter task ID to delete:\t"))
    data["tasks"] = [task for task in data["tasks"] if task["id"] != task_id]
    save_tasks(data)
    print(str(task_id) + " Task deleted")

def edit_task(data):
    if not data["tasks"]:
        print("No tasks found")
        return
    
    view_task(data)
    task_id = int(input("\nEnter task ID to edit:\t"))
    task = next((t for t in data["tasks"] if t["id"] == task_id), None)
    if not task:
        print("Task not found")
        return
    
    print(f"\nEditing Task [{task_id}] — leave blank to keep current value")
 
    new_sub = input(f"Subject [{task['subject']}]:\t").strip()
    new_topic = input(f"Topic [{task['topic']}]:\t").strip()
    new_assign = input(f"Assigning Date [{task['assign_date']}]:\t").strip()
    new_due = input(f"Due Date [{task['due_date']}]:\t").strip()
    new_priority = input(f"Priority [{task['priority']}] (1-10):\t").strip()
 
    if new_sub:
        task["subject"] = new_sub
    if new_topic:
        task["topic"] = new_topic
    if new_assign:
        task["assign_date"] = new_assign
    if new_due:
        task["due_date"] = new_due
    if new_priority:
        task["priority"] = int(new_priority)
 
    save_tasks(data)
    print(f"Task {task_id} updated successfully")

def filter_sort_tasks(data):
    if not data["tasks"]:
        print("No tasks found")
        return
    
    print("\n--Filter--")
    print("1. All tasks")
    print("2. Pending only")
    print("3. Completed only")
    filter_choice = input("Choose filter:\t").strip()

    if filter_choice == "2":
        filtered = [t for t in data["tasks"] if t["status"] == "Pending"]
    elif filter_choice == "3":
        filtered = [t for t in data["tasks"] if t["status"] == "Completed"]
    else:
        filtered = list(data["tasks"])

    print("\n-- Sort --")
    print("1. No sorting")
    print("2. Sort by priority (high to low)")
    print("3. Sort by due date (earliest first)")
    sort_choice = input("Choose sort:\t").strip()

    if sort_choice == "2":
        filtered.sort(key=lambda t: t["priority"], reverse=True)
    elif sort_choice == "3":
        def parse_data(date):
            try:
                day, month, year = date.split("-")
                return (int(day), int(month), int(year))
            except:
                return (99, 99, 9999)
        filtered.sort(key=lambda t: parse_data(t["due_date"]))

    if not filtered:
        print("No tasks match the selected filter")
    else:
        view_task(data, tasks=filtered)