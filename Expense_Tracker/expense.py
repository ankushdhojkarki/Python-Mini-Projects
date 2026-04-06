from datetime import datetime
class Expense: 
    def __init__(self, category, name, amount, date = None, time = None):
        now = datetime.now()
        self.date = now.strftime("%Y-%m-%d")
        self.time = now.strftime("%I:%M %p")
        self.category = category
        self.name = name
        self.amount = amount
        
    
    def __str__(self):
        return f"\nExpense: {self.date} | {self.time} | {self.category} | {self.name} | ${self.amount:.2f} "
