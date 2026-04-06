from expense import Expense

def main():
    print(f"Running Expense Tracker!")

    # Get user input for expense
    expense = get_user_expense()
    print(expense)

    # Write their expense to a file.
    save_expense_to_file()

    # Read file and summarize expenses.
    summarize_expenses()


def get_user_expense():
    expense_name = input("Enter expense name: ")
    expense_amount = int(input("Enter the expense amount: "))
    expense_category = [
        "🍔 Food",
        "🚌 Transport",
        "💡 Bills & Utilities",
        "🏠 Rent",
        "🛍️  Shopping",
        "🎬 Entertainment",
        "🏥 Health",
        "📚 Education"
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_category):
            print(f" {i+1}. {category_name}")
        value_range = f"[1 - {len(expense_category)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if selected_index in range(len(expense_category)):
            selected_category = expense_category[selected_index]
            new_expense = Expense(name = expense_name, category = selected_category, amount = expense_amount )
            return new_expense
        else:
            print("Invalid category. Please try again!")


def save_expense_to_file():
    print(f"Saving User Expense")

def summarize_expenses():
    print(f"Summarizing User Expense")

if __name__ == "__main__":
    main()