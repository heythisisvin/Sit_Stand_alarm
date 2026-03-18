import datetime
import time
from inputimeout import inputimeout, TimeoutOccurred #this module for unattended input.
import sys
#sys for the sys.stdout.write instead of print, to make the output in the same line.
#and make it exe using pyinstaller --noconsole --onefile Sit_and_alarm_Rev1.py

#This module get the time from midnight in minutes.
def minutes_since_midnight():
    now = datetime.datetime.now()
    midnight = datetime.datetime(now.year, now.month, now.day)
    return (now - midnight).seconds // 60

#This module get the current time in minutes.
def time_now():
    now1 = datetime.datetime.now()
    current_time_in_minutes = now1.hour * 60 + now1.minute
    return current_time_in_minutes

#This module start the alarm and check if the time is up to stand up,
# if it is, it will print the message and start the sit down alarm.
def alarm_condition_start():
    increment_stop = False
    alarm_condition_stop = minutes_since_midnight() + 60
    while increment_stop == False:
        if alarm_condition_stop == time_now():
            sys.stdout.write("Time to stand up!")
            increment_stop = True

#This module is the sit down alarm, it will ask the user if they want to exit the alarm,
# if they don't, it will print the message and start the timer for 1 minute, after that it will ask again.
def sit_down_alarm():
    sit_alarm =True
    while sit_alarm == True:
        try:
            choice_sit = inputimeout(prompt="Do you want exit this? (y/n): ", timeout=6000).lower()
            if choice_sit == "y":
                break
            else:
                sys.stdout.write("Time to sit down!")
                time.sleep(6000)
        except TimeoutOccurred:
            sys.stdout.write("Time to sit down!")
            time.sleep(6000)
        break

#This is the main loop of the program, it will start the alarm and check
# if the time is up to stand up, if it is, it will print the message and start the sit down alarm.
def start_alarm():
    alarm_start = True
    while alarm_start == True:
        alarm_condition_start()
        sit_down_alarm()

start_alarm()







