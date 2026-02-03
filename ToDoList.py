tasks = []

def show_menu():
    print("\n ---Input the List that you want ---")
    print("\n       --- To-Do List Menu ---")
    print("\n1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Quit")

def add_task():
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added!")
    else:
        print("Task cannot be empty.")

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Task '{removed}' removed!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


while True:
    show_menu()
    choice = input("\nChoose an option (1-4): ").strip()
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1-4.")