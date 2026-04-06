from expense import Expense
import datetime
import calendar

def main():
    print(f"\n{'-'*15} Expense Tracker {'-'*15}\n")
    expense_file = "Expense_Tracker/expenses.csv"
    budget = 2000

    # Get user input for expense
    expense = get_user_expense()

    # Write their expense to a file.
    save_expense_to_file(expense, expense_file)

    # Read file and summarize expenses.
    summarize_expenses(expense_file, budget)


def get_user_expense():
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter the expense amount: "))
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
        print("\nSelect a category: ")
        for i, category_name in enumerate(expense_category):
            print(f" {i+1}. {category_name}")
        value_range = f"[1 - {len(expense_category)}]"
        selected_index = int(input(f"\nEnter a category number {value_range}: ")) - 1

        if selected_index in range(len(expense_category)):
            selected_category = expense_category[selected_index]
            new_expense = Expense(name = expense_name, category = selected_category, amount = expense_amount )
            return new_expense
        else:
            print("Invalid category. Please try again!")


def save_expense_to_file(expense, expense_file):
    print(f"\nSaving User Expense:{expense} to {expense_file}")
    with open(expense_file, "a", encoding="utf-8") as f:
        f.write(f"{expense.date}, {expense.time}, {expense.category}, {expense.name}, {expense.amount}\n")

def summarize_expenses(expense_file, budget):
    print(f"\nSummarizing User Expense")
    expenses = []
    with open(expense_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            expense_date, expense_time, expense_category, expense_name, expense_amount = line.strip().split(",")
            line_expense = Expense(
                date = expense_date,
                time = expense_time,
                category = expense_category,
                name = expense_name,
                amount = float(expense_amount),
            )
            expenses.append(line_expense)
    
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    
    print("\nExpenses By Category:")
    for key, amount in amount_by_category.items():
        print(f"  {key}: ${amount:.2f}")
    
    total_spent = sum([x.amount for x in expenses])
    print(f"\n💸 Total Spent: ${total_spent:.2f}")

    remaining_budget = budget - total_spent
    print(f"✅ Remaining Budget: ${remaining_budget:.2f}")

    # Get the current date
    now = datetime.datetime.now()

    # Get the number of days in the current month
    days_in_month = calendar.monthrange(now.year, now.month)[1]

    # Calculate the remaining number of days in the current month
    remaining_days = days_in_month - now.day

    daily_budget = remaining_budget / remaining_days
    print(f"👉 Daily Budget: ${daily_budget:.2f}")

if __name__ == "__main__":
    main()