import json
import os
import matplotlib.pyplot as plt

# Load expenses if file exists
if os.path.exists("expenses.json"):
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except json.JSONDecodeError:
        print("The file was empty or corrupted. Starting fresh...")
        expenses = {}
else:
    expenses = {}

# Function to save expenses
def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

# Main program loop
while True:
    try:
        print("\n" + "="*40)
        print("       EXPENSE TRACKER MENU")
        print("="*40)
        print("1. Add Expenses")
        print("2. View Expenses")
        print("3. View Total Spent")
        print("4. Remove a Specific Expense")
        print("5. View Pie Chart")
        print("6. Exit")
        print("="*40)

        user_choice = int(input("Choose an option [1-6]: "))

        # Add Expenses
        if user_choice == 1:
            user_choice_category = input("Enter the category: ").title().strip()
            if user_choice_category not in expenses:
                expenses[user_choice_category] = []

            user_choice_item = input("Enter the item name: ").title().strip()
            user_choice_amount = float(input("Enter the amount: "))
            expenses[user_choice_category].append((user_choice_item, user_choice_amount))
            save_expenses()
            print(f"\n✅ Expense '{user_choice_item}' added under '{user_choice_category}' for ${user_choice_amount:.2f}")

        # View Expenses
        elif user_choice == 2:
            if not expenses:
                print("\n⚠️  No expenses yet.")
            else:
                print("\n📋 Your Expenses:")
                for category, items in expenses.items():
                    print(f"\n--- {category} ---")
                    for item, amount in items:
                        print(f"• {item}: ${amount:.2f}")

        # View Total Spent
        elif user_choice == 3:
            if not expenses:
                print("\n⚠️  No expenses yet.")
            else:
                total_spent = sum(amount for items in expenses.values() for _, amount in items)
                print(f"\n💰 Total Expenses: ${total_spent:.2f}")

        # Remove a Specific Expense
        elif user_choice == 4:
            if not expenses:
                print("\n⚠️  No expenses yet.")
            else:
                print("\nAvailable Categories:")
                for category in expenses.keys():
                    print(f"- {category}")

                user_selection_category = input("Enter the category: ").title().strip()

                if user_selection_category in expenses:
                    items_in_category = expenses[user_selection_category]
                    if not items_in_category:
                        print(f"No expenses under {user_selection_category}.")
                    else:
                        print(f"\nExpenses in {user_selection_category}:")
                        for i, (item, amount) in enumerate(items_in_category, 1):
                            print(f"{i}. {item}: ${amount:.2f}")

                        try:
                            item_to_remove = int(input("Enter the number of the item you want to remove: "))
                            if 1 <= item_to_remove <= len(items_in_category):
                                removed_item = items_in_category.pop(item_to_remove - 1)
                                print(f"\n✅ '{removed_item[0]}' removed successfully from '{user_selection_category}'")
                                save_expenses()
                            else:
                                print("❌ Invalid item number.")
                        except ValueError:
                            print("❌ Invalid input. Please enter a number.")
                else:
                    print("❌ Category does not exist!")

        # View Pie Chart
        elif user_choice == 5:
            if not expenses:
                print("\n⚠️  No expenses yet.")
            else:
                categories = []
                totals = []

                for category, items in expenses.items():
                    total = sum(amount for _, amount in items)
                    categories.append(category)
                    totals.append(total)

                print("\n📊 Pie Chart of Expenses")
                colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#ffb3e6','#c2c2f0','#ff6666']
                plt.figure(figsize=(7,7))
                plt.pie(totals, labels=categories, autopct="%1.1f%%", colors=colors, startangle=90)
                plt.title("Expenses by Category")
                plt.axis('equal')
                plt.show()

        # Exit
        elif user_choice == 6:
            save_expenses()
            print("\n👋 Goodbye!")
            break

        else:
            print("❌ Please choose a valid option between 1 and 6.")

    except ValueError:
        print("❌ Invalid input! Please enter a number.")
