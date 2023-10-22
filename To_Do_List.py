import os

# Initialize an empty to-do list
todo_list = []

# Function to display the to-do list
def display_todo_list():
    if len(todo_list) == 0:
        print("Your to-do list is empty.")
    else:
        print("Your To-Do List:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

# Function to add a task to the to-do list
def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added to your to-do list.")

# Function to remove a task from the to-do list
def remove_task(index):
    if 1 <= index <= len(todo_list):
        removed_task = todo_list.pop(index - 1)
        print(f"Task '{removed_task}' removed from your to-do list.")
    else:
        print("Invalid task index. Task not removed.")

# Main loop
while True:
    print("\nOptions:")
    print("1. Display To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        display_todo_list()
    elif choice == '2':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '3':
        display_todo_list()
        index = int(input("Enter the index of the task to remove: "))
        remove_task(index)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please choose a valid option.")

# Save the to-do list to a file for future use (optional)
with open('todo_list.txt', 'w') as file:
    for task in todo_list:
        file.write(task + '\n')

print("To-Do List program has ended.")
