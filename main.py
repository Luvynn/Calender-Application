from tkinter import *
from PIL import ImageTk, Image
import calendar
import datetime

# Initialize the main window
root = Tk()
root.geometry('480x550')
root.title('Interactive Calendar')
root.config(background="#f9f9f9")
root.resizable(0, 0)

# Get current month and year
now = datetime.datetime.now()
current_month = now.month
current_year = now.year

# Functions to handle month and year navigation
def display_calendar(year, month):
    output = calendar.TextCalendar().formatmonth(year, month)
    cal_label.config(text=output)

def prev_month():
    global current_month, current_year
    if current_month == 1:
        current_month = 12
        current_year -= 1
    else:
        current_month -= 1
    display_calendar(current_year, current_month)

def next_month():
    global current_month, current_year
    if current_month == 12:
        current_month = 1
        current_year += 1
    else:
        current_month += 1
    display_calendar(current_year, current_month)

def reset_to_today():
    global current_month, current_year
    current_month = now.month
    current_year = now.year
    display_calendar(current_year, current_month)

def close_app():
    root.quit()

# Top Header
header_frame = Frame(root, bg="#4B77BE", height=70)
header_frame.pack(fill=X)

header_label = Label(header_frame, text="Business Calendar", font=("Segoe UI", 24, "bold"), fg="white", bg="#4B77BE")
header_label.pack(pady=10)

# Month and Year Display
nav_frame = Frame(root, bg="#f9f9f9")
nav_frame.pack(pady=10)

prev_button = Button(nav_frame, text="<<", font=("Segoe UI", 14), command=prev_month, bg="#3498DB", fg="white", padx=10, pady=5)
prev_button.grid(row=0, column=0, padx=20)

next_button = Button(nav_frame, text=">>", font=("Segoe UI", 14), command=next_month, bg="#3498DB", fg="white", padx=10, pady=5)
next_button.grid(row=0, column=2, padx=20)

# Current Month and Year Label
current_month_label = Label(nav_frame, text="Month", font=("Segoe UI", 16), bg="#f9f9f9")
current_month_label.grid(row=0, column=1, padx=10)

# Calendar Display Label
cal_label = Label(root, font=("Courier", 16), bg="white", justify=LEFT, relief=RIDGE, width=24, height=10)
cal_label.pack(pady=15)

# Bottom Controls
button_frame = Frame(root, bg="#f9f9f9")
button_frame.pack(pady=20)

reset_button = Button(button_frame, text="Today", font=("Segoe UI", 14), command=reset_to_today, bg="#2ECC71", fg="white", padx=10, pady=5)
reset_button.grid(row=0, column=0, padx=20)

exit_button = Button(button_frame, text="Exit", font=("Segoe UI", 14), command=close_app, bg="#E74C3C", fg="white", padx=15, pady=5)
exit_button.grid(row=0, column=1, padx=20)

# Display the current month initially
display_calendar(current_year, current_month)

# Run the main loop
root.mainloop()
