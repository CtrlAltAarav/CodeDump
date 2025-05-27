# todo_list
todo = []

while True:
    task = input("Enter task (or 'exit' to quit): ")
    if task.lower() == 'exit':
        break
    todo.append(task)

print("\nYour To-Do List:")
for i, task in enumerate(todo, 1):
    print(f"{i}. {task}")
