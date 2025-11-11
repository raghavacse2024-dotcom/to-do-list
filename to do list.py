import sys

todo_list = []

def show_menu():
    print("""
--------- To-Do List Menu ---------
1. View Tasks
2. Add Task
3. Remove Task
4. Mark Task as Done
5. Edit Task
6. Search Tasks
7. Sort Tasks by Priority
8. View Completed Tasks
9. Exit
""")

def view_tasks(show_completed=False):
    tasks = [task for task in todo_list if task['done'] == show_completed] if show_completed else [task for task in todo_list if not task['done']]
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks, start=1):
            status = "✓" if task['done'] else " "
            print(f"{idx}. [{status}] {task['name']} [Category: {task['category']}, Priority: {task['priority']}]")

def add_task():
    name = input("Task name: ")
    category = input("Category (e.g., work, personal): ")
    priority = input("Priority (High/Medium/Low): ").capitalize()
    todo_list.append({"name": name, "category": category, "priority": priority, "done": False})
    print("Task added.")

def remove_task():
    view_tasks()
    try:
        idx = int(input("Task number to remove: ")) - 1
        removed = todo_list.pop(idx)
        print(f"Removed task: {removed['name']}")
    except (ValueError, IndexError):
        print("Invalid selection.")

def mark_done():
    view_tasks()
    try:
        idx = int(input("Task number to mark as done: ")) - 1
        todo_list[idx]['done'] = True
        print("Task marked as done.")
    except (ValueError, IndexError):
        print("Invalid selection.")

def edit_task():
    view_tasks()
    try:
        idx = int(input("Task number to edit: ")) - 1
        print("Leave blank to keep current value.")
        name = input(f"New name (current: {todo_list[idx]['name']}): ")
        category = input(f"New category (current: {todo_list[idx]['category']}): ")
        priority = input(f"New priority (current: {todo_list[idx]['priority']}): ")
        if name:
            todo_list[idx]['name'] = name
        if category:
            todo_list[idx]['category'] = category
        if priority:
            todo_list[idx]['priority'] = priority.capitalize()
        print("Task updated.")
    except (ValueError, IndexError):
        print("Invalid selection.")

def search_tasks():
    query = input("Search keyword: ").lower()
    results = [task for task in todo_list if query in task['name'].lower()]
    if not results:
        print("No matching tasks found.")
    else:
        for idx, task in enumerate(results, start=1):
            status = "✓" if task['done'] else " "
            print(f"{idx}. [{status}] {task['name']} [Category: {task['category']}, Priority: {task['priority']}]")

def sort_tasks():
    todo_list.sort(key=lambda x: {"High": 0, "Medium": 1, "Low": 2}.get(x['priority'], 3))
    print("Tasks sorted by priority.")

def main():
    while True:
        show_menu()
        choice = input("Select an option (1-9): ")
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_done()
        elif choice == "5":
            edit_task()
        elif choice == "6":
            search_tasks()
        elif choice == "7":
            sort_tasks()
        elif choice == "8":
            view_tasks(show_completed=True)
        elif choice == "9":
            print("Exiting To-Do List App.")
            sys.exit()
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
