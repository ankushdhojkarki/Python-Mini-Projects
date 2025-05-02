🎯 Drink Water Reminder – Desktop Notification App
A simple Python script that reminds you to drink water every hour using desktop notifications. It runs in the background and helps promote healthy hydration habits.

📌 How It Works

The script continuously runs in a loop.

Every hour, it prints a message and sends a desktop notification reminding you to drink water.

The notification appears using the plyer library's notification module.

📁 Files Included
drink_water_reminder.py — The main Python script that sends hourly water reminders.

▶️ How to Run

Make sure you have Python installed.

Install the required package:

bash
Copy code
pip install plyer
Run the script:

bash
Copy code
python drink_water_reminder.py
💡 This script must be left running in the terminal to keep receiving hourly notifications.

📎 Tip: You can customize the interval by modifying the time.sleep(60*60) line to suit your preference.
