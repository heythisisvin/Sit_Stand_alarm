import datetime
import time

def minutes_since_midnight():
    now = datetime.datetime.now()
    midnight = datetime.datetime(now.year, now.month, now.day)
    return (now - midnight).seconds // 60
def time_now():
    now1 = datetime.datetime.now()
    current_time_in_minutes = now1.hour * 60 + now1.minute
    return current_time_in_minutes
def alarm_condition_start():
    increment_stop = False
    alarm_condition_stop = minutes_since_midnight() + 1
    print(alarm_condition_stop)
    while increment_stop == False:
        if alarm_condition_stop == time_now():
            print("Time to stand up!")
            increment_stop = True

def sit_down_alarm():
    sit_alarm =True
    while sit_alarm == True:
        choice_sit = input("Do you want exit this? (y/n)").lower()
        if choice_sit == "y":
            exit()
        else:
            print("Time to sit down!")
            time.sleep(60)

alarm_start = True
alarm_condition_start()
while alarm_start == True:
    alarm_condition_start()
    sit_down_alarm()










