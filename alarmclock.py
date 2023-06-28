import datetime
import time

def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("ALARM!")
            break
        time.sleep(1)
print("Welcome to the Digital Alarm Clock!")
print("Please enter the alarm time in 24-hour format.")
print("Example: 08:30:00")
alarm_time = input("Enter the alarm time: ")
set_alarm(alarm_time)
