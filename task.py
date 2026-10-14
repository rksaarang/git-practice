def get_task_details():
    task_name = input("Enter task name: ")
    assigned_to = input("Enter assigned person: ")
    status = input("Enter task status: ")

    return task_name, assigned_to, status


def display_task(task_name, assigned_to, status):
    print("\n--- Task Details ---")
    print(f"Task: {task_name}")
    print(f"Assigned to: {assigned_to}")
    print(f"Status: {status}")


def main():
    task_name, assigned_to, status = get_task_details()
    display_task(task_name, assigned_to, status)


if __name__ == "__main__":
    main()