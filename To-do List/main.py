
tasks = []


def user():
    print("***** Welcome to the To-Do APP *****\n")

    name = input("Kindly enter your name here: ")

    while True:
        print(f"\nWhat would you like to do, {name}?")

        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Quit")

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            task = input("Enter your task: \n")
            tasks.append(task)
            print("Your task has been added successfully!")

        elif choice == 2:
            print("\nYour Tasks:")
            if tasks:
                for index, task in enumerate(tasks, 1):
                    print(f"{index}. {task}")
            else:
                print("No tasks to show.")

        elif choice == 3:
            if tasks:
                print("\nYour Tasks:")
                for index, task in enumerate(tasks, 1):
                    print(f"{index}. {task}")
                try:
                    remove_index = int(
                        input("Enter the task number you wish to remove: "))
                    if 1 <= remove_index <= len(tasks):
                        removed = tasks.pop(remove_index - 1)
                        print(f"Removed Task: {removed}")
                    else:
                        print("Invalid Task Number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("No tasks to remove.")

        elif choice == 4:
            print(f"Goodbye, {name}!")
            break

        else:
            print("Invalid choice. Kindly choose from 1-4.")


user()
