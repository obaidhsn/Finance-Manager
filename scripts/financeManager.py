class Transaction:
    def __init__(self, date, amount, category, description):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description

    def __str__(self):
        return f"{self.date} - {self.amount} - {self.category} - {self.description}"

class FinanceManager:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_transactions(self):
        return self.transactions

    def get_total_income(self):
        return sum([t.amount for t in self.transactions if t.amount > 0])

    def get_total_expense(self):
        return sum([t.amount for t in self.transactions if t.amount < 0])

    def get_category_wise_expense(self):
        expenses = {}
        for t in self.transactions:
            if t.amount < 0:
                if t.category in expenses:
                    expenses[t.category] += t.amount
                else:
                    expenses[t.category] = t.amount
        return expenses
