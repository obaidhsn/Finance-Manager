from scripts import financeManager
from flask import Flask

app = Flask("Finance Manager")

if __name__ == "__main__":
    app.run()

    manager = financeManager.FinanceManager()

    while True:
        print("""
        Personal Finance Manager:
        1. Add Transaction
        2. Show Transactions
        3. Show Total Income
        4. Show Total Expense
        5. Show Category-wise Expense
        6. Quit
        """)

        choice = int(input("Enter your choice: "))

        if choice == 1:
            date = input("Enter date (dd/mm/yyyy): ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            transaction = Transaction(date, amount, category, description)
            manager.add_transaction(transaction)
            print("Transaction added.")
        elif choice == 2:
            transactions = manager.get_transactions()
            print("Transactions:")
            for t in transactions:
                print(t)
        elif choice == 3:
            total_income = manager.get_total_income()
            print(f"Total Income: {total_income}")
        elif choice == 4:
            total_expense = manager.get_total_expense()
            print(f"Total Expense: {total_expense}")
        elif choice == 5:
            category_wise_expense = manager.get_category_wise_expense()
            print("Category-wise Expense:")
            for category, amount in category_wise_expense.items():
                print(f"{category}: {amount}")
        elif choice == 6:
            break
        else:
            print("Invalid choice.")

    print("Goodbye!")