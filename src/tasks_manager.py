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
        "id": len(data["tasks"]) + 1,
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

def view_task(data):
    if not data["tasks"]:
        print("No tasks added yet")
        return
    for task in data["tasks"]:
        print(f"\n[{task["id"]}] {task["subject"]} - {task["topic"]}")
        print(f"Due: {task["due_date"]} | Priority: {task["priority"]} | Status: {task["status"]}")
        if task["status"] == "Completed":
            inp = input("Date of Completion (DD-MM-YYY):\t")
            task["complete_date"] = inp
            print(f"Completion Date: {task["complete_date"]}")

def mark_complete(data):
    view_task(data)
    task_id = int(input("\nEnter task ID to mark its completion:\t"))
    for task in data["tasks"]:
        if task["id"] == task_id:
            task["status"] = "Completed"
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