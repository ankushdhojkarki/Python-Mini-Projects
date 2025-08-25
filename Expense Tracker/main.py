import json
import os

if os.path.exists("expenses.json"):

    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except json.JSONDecodeError:
        print(f"The file was expty or corrupted. Starting fresh...")
        expenses = {}

else:        
    expenses = {}

def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent = 4)    

while True:
    try:
        print(f"\n\n      MENU\n\n1. Add Expenses\n2. View Expenses\n3. View Total Spent\n4.Remove a Specific Expense\n5. Exit\n")
        user_choice = int(input("\nChoose an option from the menu [1 - 5]: "))

        if user_choice == 1:  # Add category, expense, and amount
            user_choice_category = input("Enter the category: ").title().strip()
            if user_choice_category not in expenses:
                expenses[user_choice_category] = []

            user_choice_item = input("Enter the item name: ").title().strip()
            user_choice_amount = int(input("Enter the amount: "))
            expenses[user_choice_category].append((user_choice_item, user_choice_amount))
            save_expenses()

        elif user_choice == 2:  # View category and expenses
            if len(expenses) == 0:
                print("No expenses yet.")
            else:
                print("Here are your expenses: \n")
                for category in expenses:
                    print(category)
                    for item, amount in expenses[category]:
                        print(f"- {item} : {amount}")
                    print()

        elif user_choice == 3:  # View total money spent
            if len(expenses) == 0:
                print("No expenses yet.")
            else:
                total_spent = 0
                for category in expenses:
                    for item, amount in expenses[category]:
                        total_spent += amount
                print(f"Total Expenses: {total_spent}")

        elif user_choice == 4:  # Remove a specific expense
            if len(expenses) == 0:
                print("No expenses yet.")
            else:
                print("Available Categories:")
                for category in expenses:
                    print("-", category)

                user_selection_category = input("Enter the category: ").title().strip()

                if user_selection_category in expenses:
                    if len(expenses[user_selection_category]) == 0:
                        print(f"No expenses under {user_selection_category}.")
                    else:
                        print(f"Expenses in {user_selection_category}:")
                        for item, amount in expenses[user_selection_category]:
                            print(f"- {item} : {amount}")

                        user_selection_item_remove = input("Enter the item you want to remove: ").strip().lower()
                        found = False
                        for expense in expenses[user_selection_category]:
                            if expense[0].lower() == user_selection_item_remove:
                                expenses[user_selection_category].remove(expense)
                                print(f"{expense[0]} has been removed successfully.")
                                save_expenses()
                                found = True
                                break

                        if not found:
                            print("Expense not found.")
                else:
                    print("Category does not exist!")

        elif user_choice == 5:  # Exit the program
            print("Goodbye!")
            break

        else:
            print("Please choose a valid option between 1 and 5.")

    except ValueError:
        print("Invalid input! Please enter a number between 1 and 5.")
