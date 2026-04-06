from datetime import datetime
class Expense: 
    def __init__(self, category, amount, description):
        now = datetime.now()
        self.date = now.strftime("%Y-%m-%d")
        self.time = now.strftime("%I:%M %p")
        self.category = category
        self.amount = amount
        self.description = description
    
    def __str__(self):
        return f"{self.date} | {self.time} | {self.category} | {self.amount} | {self.description}"

e1 = Expense("food", 200, "momo")
print(e1)