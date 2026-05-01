# Simple Python To-Do List for IS Assignment
tasks = []

def show_tasks():
    print("\n--- CURRENT TASKS ---")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}")

print("Welcome to your Semester Task Manager!")
while True:
    new_task = input("\nEnter a task (or type 'quit' to exit): ")
    if new_task.lower() == 'quit':
        break
    tasks.append(new_task)
    show_tasks()

print("Great job staying organized!")
