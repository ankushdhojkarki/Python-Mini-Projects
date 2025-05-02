🎯 Drink Water Reminder  
This is a terminal-based Python script that sends a desktop notification every hour reminding you to drink water. It's a simple wellness tool that helps you stay hydrated throughout your work or study sessions.

📌 How It Works  
- The script runs in an infinite loop.  
- Every hour (`60 * 60` seconds), it prints a message in the terminal.  
- Simultaneously, it uses `plyer` to show a desktop notification with a hydration reminder.  

📁 Files Included  
- `drink_water_reminder.py` — The main script that triggers hourly reminders using terminal print and desktop notifications.

▶️ How to Run  
Make sure you have Python installed.

1. Install the required package:

```bash
pip install plyer
