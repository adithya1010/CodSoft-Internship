'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

# To-do list
tasks = []
def add_task(task):
    tasks.append(task)

def remove_task(task):
    if task in tasks:
        tasks.remove(tasks)
        print("Task removed successfully")
    else:
        print("Task not found")

def display_tasks():
    if not tasks:
        print("No tasks found")
    else:
        print("Tasks:")
        for(index, task) in enumerate(tasks, start=1):
            print(f"{index}.{task}")

def main():
    while True:
        print("\n Options:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Display tasks")
        print("4. Exit")
        choice = input("Enter your choice:")
        if choice == "1":
            task = input("Enter the task to be added:")
            add_task(task)
        elif choice == "2":
            task = input("Enter the task to be removed:")
            remove_task(task)
        elif choice == "3":
            display_tasks()
        elif choice == "4":
            print("Exiting the application")
            break
        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()

