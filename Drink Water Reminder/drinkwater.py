import time
from plyer import notification

while True:
    print("Please sip some water!")
    notification.notify(title="Reminder to drink water",
                        message="Please drink some water to stay hydrated.")
    time.sleep(3)  # 1 hour reminder
