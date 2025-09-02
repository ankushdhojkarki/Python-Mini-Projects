import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QDialog, QLineEdit, QLabel, QFormLayout, QHBoxLayout

app = QApplication(sys.argv) 

#Create blank window
window = QWidget()
window.setWindowTitle(" Expense Tracker ")
window.resize(400, 300)


layout = QVBoxLayout() #Create Layout

btn_add_expense = QPushButton("➕ Add Expense") #Create Buttons
btn_view_expense = QPushButton("👀 View Expenses")
btn_total_spent = QPushButton("💰 Total Spent")
btn_remove_specific_expense = QPushButton("🗑️ Remove Specific Expense")
btn_view_pie_chart = QPushButton("📊 View Pie Chart")

btn_exit = QPushButton("👋 Exit")

layout.addWidget(btn_add_expense) #Adds each button into the vertical layout (one below the other)
layout.addWidget(btn_view_expense) 
layout.addWidget(btn_total_spent)
layout.addWidget(btn_remove_specific_expense)
layout.addWidget(btn_view_pie_chart)
layout.addWidget(btn_exit)


window.setLayout(layout) #Attach layout to the window

btn_exit.clicked.connect(app.quit) #Connects Exit Button to action --> When Exit BUtton is clicked, app.quit() runs and the app closes


window.show() #Show the window
sys.exit(app.exec_()) 
