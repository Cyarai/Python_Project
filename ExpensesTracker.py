import json
import os
from datetime import datetime


EXPENSES_FILE = 'expenses.json'

def load_expenses():
    
    if os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, 'r') as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    
    with open(EXPENSES_FILE, 'w') as f:
        json.dump(expenses, f, indent=4)

def add_expense(expenses):
    
    description = input("Enter expense description: ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if not date:
        date = datetime.now().strftime('%Y-%m-%d')
    expense = {
        'description': description,
        'amount': amount,
        'date': date
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")

def view_expenses(expenses):
    
    if not expenses:
        print("No expenses recorded.")
        return
    total = 0
    print("\nExpenses:")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['date']} - {exp['description']}: ${exp['amount']:.2f}")
        total += exp['amount']
    print(f"\nTotal spent: ${total:.2f}")

def main():
    expenses = load_expenses()
    while True:
        print("\nExpenses Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()