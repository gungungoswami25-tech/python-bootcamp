
tasks = []
task_id = 1


def add_task():
    global task_id

    title = input("Enter task name: ")

    if title.strip() == "":
        print("Task cannot be empty!")
        return

    task = {
        "id": task_id,
        "title": title,
        "completed": False
    }

    tasks.append(task)
    task_id += 1

    print("Task added successfully!")


def view_tasks():
    if len(tasks) == 0:
        print("No tasks available!")
        return

    print("\n===== YOUR TASKS =====")

    for task in tasks:
        if task["completed"]:
            status = "Completed"
        else:
            status = "Pending"

        print(
            task["id"],
            task["title"],
            "-",
            status
        )


def update_task():
    view_tasks()

    if len(tasks) == 0:
        return

    task_id = int(input("Enter task ID to update: "))

    for task in tasks:
        if task["id"] == task_id:
            new_title = input("Enter new task name: ")

            if new_title.strip() == "":
                print("Task name cannot be empty!")
                return

            task["title"] = new_title
            print("Task updated successfully!")
            return

    print("Task not found!")


def delete_task():
    view_tasks()

    if len(tasks) == 0:
        return

    task_id = int(input("Enter task ID to delete: "))

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print("Task deleted successfully!")
            return

    print("Task not found!")


def complete_task():
    view_tasks()

    if len(tasks) == 0:
        return

    task_id = int(input("Enter task ID to complete: "))

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            print("Task marked as completed!")
            return

    print("Task not found!")


def main():
    while True:
        print("\n===== BETTER TODO APP =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark as Completed")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            update_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            complete_task()

        elif choice == "6":
            print("Thank you for using Todo App!")
            break

        else:
            print("Invalid choice!")


main()
