import json
import os

# Load existing tasks from a file
def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            return json.load(f)
    else:
        return []

# Save tasks to a file
def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

# Show all tasks
def show_tasks(tasks):
    if not tasks:
        print("No tasks available!")
    for index, task in enumerate(tasks):
        status = "Done" if task["completed"] else "Pending"
        print(f"{index+1}. {task['description']} (Due: {task['due_date']}) - {status}")

# Add a task
def add_task(tasks):
    description = input("Enter task description: ")
    due_date = input("Enter due date (e.g., YYYY-MM-DD): ")
    tasks.append({"description": description, "due_date": due_date, "completed": False})
    print("Task added!")
    save_tasks(tasks)

# Mark task as completed
def complete_task(tasks):
    show_tasks(tasks)
    task_id = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= task_id < len(tasks):
        tasks[task_id]["completed"] = True
        print("Task marked as completed!")
        save_tasks(tasks)
    else:
        print("Invalid task number!")

# Delete a task
def delete_task(tasks):
    show_tasks(tasks)
    task_id = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        print("Task deleted!")
        save_tasks(tasks)
    else:
        print("Invalid task number!")

# Main menu
def menu():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Application")
        print("1. Show all tasks")
        print("2. Add a task")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again!")

if __name__ == "__main__":
    menu()
