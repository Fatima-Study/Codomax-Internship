print("Simple To-Do List")

tasks = []

for i in range(3):
    task = input("Enter a task: ")
    tasks.append(task)

print("\nYour To-Do List:")

for task in tasks:
    print("-", task)
