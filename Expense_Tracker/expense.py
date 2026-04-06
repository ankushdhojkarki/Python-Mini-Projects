from datetime import datetime
class Expense: 
    def __init__(self, name, category, amount):
        now = datetime.now()
        self.date = now.strftime("%Y-%m-%d")
        self.time = now.strftime("%I:%M %p")
        self.name = name
        self.category = category
        self.amount = amount
        
    
    def __str__(self):
        return f"Expense: {self.date} | {self.time} | | {self.name} {self.category} | ${self.amount:.2f} "
