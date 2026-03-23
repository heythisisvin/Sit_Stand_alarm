import tkinter as tk
import tkinter.messagebox as messagebox


root = tk.Tk()
root.withdraw()  # Hide the main window

STAND_UP_INTERVAL = 3600000  #interval in milliseconds to show the "Tumayo ka" window (1 hour)
SIT_DOWN_INTERVAL = 300000
AUTO_CLOSE = 300000  # Time in milliseconds to auto-close the window (5 minute)

def on_closing(window):
    # 1. Ask user or perform cleanup
    if messagebox.askyesno("Quit", "Do you want to quit this window?."):
        window.destroy()  # Finally, destroy the window
    else:
        pass # Show the window again if user cancels

def tumayo_ka():#use toplevel for subwindows
    tumayo_window = tk.Toplevel(root)
    tumayo_window.title("Tumayo ka. Tangina Ka!")
    tumayo_window.geometry("300x200")
    my_label = tk.Label(tumayo_window, text="Tumayo Ka, Tangina Ka!!", font=("Helvetica", 14))
    # Centered using place (x and y relative to 0-1)
    my_label.place(relx=0.5, rely=0.5, anchor="center")
    tumayo_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(tumayo_window))  # Override close button for this window
    tumayo_window.after(AUTO_CLOSE, tumayo_window.destroy)  # Automatically close after 1 minute (60000 milliseconds)

    root.after(SIT_DOWN_INTERVAL, umupo_ka)  # Schedule the next window after sitting down interval

def umupo_ka():#use toplevel for subwindows
    umupo_window = tk.Toplevel(root)
    umupo_window.title("Umupo kana, Bwesit ka!")
    umupo_window.geometry("300x200")
    my_label = tk.Label(umupo_window, text="Umupo kana, Bwesit ka!!", font=("Helvetica", 14))
    # Centered using place (x and y relative to 0-1)
    my_label.place(relx=0.5, rely=0.5, anchor="center")
    umupo_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(umupo_window))
    umupo_window.after(AUTO_CLOSE, umupo_window.destroy)  # Automatically close after 1 minute (60000 milliseconds)

    root.after(STAND_UP_INTERVAL, tumayo_ka)  # Schedule the next window after stand up interval


root.after(STAND_UP_INTERVAL, tumayo_ka)  # Check the alarm condition every second

root.mainloop()




