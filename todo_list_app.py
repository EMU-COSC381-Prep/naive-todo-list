# Minimal To-Do List App

def show_menu():
    """Display the menu options."""
    print("\nTo-Do List App")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Exit")

def view_tasks(tasks):
    """Display all tasks in the to-do list."""
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    """Add a new task to the to-do list."""
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def main():
    """Main function to run the to-do list app."""
    tasks = []  # List to store tasks
    while True:
        show_menu()
        choice = input("Choose an option (1-3): ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
