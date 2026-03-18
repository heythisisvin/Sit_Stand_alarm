import tkinter as tk
from tkinter import messagebox
import Modules
from inputimeout import inputimeout, TimeoutOccurred
import time


def sit_down_alarm():
    sit_alarm =True
    while sit_alarm == True:
        try:
            choice_sit = inputimeout(prompt="Do you want exit this? (y/n): ", timeout=10).lower()
            if choice_sit == "y":
                break
            else:
                print("Time to sit down!")
                time.sleep(60)
        except TimeoutOccurred:
            print("Time to sit down!")
            time.sleep(60)
        break

def on_close():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()

def auto_close():
    root.destroy()

run = True
while run == True:
    root = tk.Tk()
    Modules.alarm_condition_start()
    root.title("Stand Alarm")
    root.geometry("300x300")
    label = tk.Label(root, text="Time to stand up!", font=("Arial", 24))
    label.pack(pady=20)
    root.protocol("WM_DELETE_WINDOW", on_close)
    root.after(6000, auto_close)
    if root.after(6000, auto_close) == True:
        alarm_window = tk.Toplevel(root)
        alarm_window.title("Reminder")
        alarm_window.geometry("300x150")
        label = tk.Label(alarm_window, text="Time to sit down!")
        label.pack(pady=20)
        root.after(6000, auto_close)
        break

    root.mainloop()

