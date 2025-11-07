# To-Do List Manager
FILE_NAME = "tasks.txt"

def add_task(task):
    """Add a new task to the list."""
    with open(FILE_NAME, 'a') as f:
        f.write(f"{task} | Incomplete\n")
    print(f"✅ Task added: {task}")

def view_tasks():
    """View all tasks."""
    try:
        with open(FILE_NAME, 'r') as f:
            tasks = f.readlines()
            if not tasks:
                print("📭 No tasks found.")
                return
            print("\n📋 To-Do List:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("⚠️ No task file found. Add a task first.")

def remove_task(task_number):
    """Remove a task by number."""
    try:
        with open(FILE_NAME, 'r') as f:
            tasks = f.readlines()
        if 0 < task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            with open(FILE_NAME, 'w') as f:
                f.writelines(tasks)
            print(f"🗑️ Task removed: {removed_task.strip()}")
        else:
            print("❌ Invalid task number.")
    except FileNotFoundError:
        print("⚠️ No task file found.")

def mark_completed(task_number):
    """Mark a task as completed."""
    try:
        with open(FILE_NAME, 'r') as f:
            tasks = f.readlines()
        if 0 < task_number <= len(tasks):
            task, status = tasks[task_number - 1].strip().split(" | ")
            if status == "Completed":
                print("✅ Task already completed.")
                return
            tasks[task_number - 1] = f"{task} | Completed\n"
            with open(FILE_NAME, 'w') as f:
                f.writelines(tasks)
            print(f"🎯 Task marked as completed: {task}")
        else:
            print("❌ Invalid task number.")
    except FileNotFoundError:
        print("⚠️ No task file found.")

# Main Menu
def main():
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            task = input("Enter new task: ")
            add_task(task)
        elif choice == '3':
            view_tasks()
            num = int(input("Enter task number to remove: "))
            remove_task(num)
        elif choice == '4':
            view_tasks()
            num = int(input("Enter task number to mark completed: "))
            mark_completed(num)
        elif choice == '5':
            print("👋 Exiting... Your tasks are saved in 'tasks.txt'.")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
