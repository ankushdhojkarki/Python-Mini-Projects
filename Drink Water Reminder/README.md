# 🎯 Drink Water Reminder – A Simple Hourly Notification in Python

This is a lightweight terminal-based Python script that reminds you to drink water every hour. It displays a message in the terminal and sends a system notification to keep you hydrated.

---

## 📌 How It Works

- The script runs an infinite loop using `while True`.
- Every hour (60 minutes), it:
  - Prints a message in the terminal: “Please sip some water!”
  - Sends a system notification using the `plyer` library.
- Keeps reminding you until you stop the script manually.

---

## 📁 Files Included

- `drink_water_reminder.py` — The main script that triggers hourly hydration reminders.

---

## ▶️ How to Run

1. Make sure you have Python installed.
2. Install the required package by running:

```bash
pip install plyer
Save the script as drink_water_reminder.py.

Open your terminal or command prompt.

Run the script using:

bash
Copy code
python drink_water_reminder.py
💡 To stop the reminder, press Ctrl + C in the terminal.
