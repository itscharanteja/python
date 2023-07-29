import tkinter as tk
from tkinter import messagebox

def start_timer():
    seconds = int(entry.get())
    start_button['state'] = 'disabled'  # Disable the button during the countdown

    for i in range(seconds, -1, -1):
        minutes = i // 60
        seconds = i % 60
        time_format = '{:02d}:{:02d}'.format(minutes, seconds)
        label['text'] = time_format
        window.update()
        window.after(1000)  # Delay for 1 second

    messagebox.showinfo('Time Up!', 'The timer has finished.')
    start_button['state'] = 'normal'  # Enable the button after the countdown

# Create the main window
window = tk.Tk()
window.title('Timer App')

# Create the GUI elements
label = tk.Label(window, text='Enter the number of seconds:')
label.pack()

entry = tk.Entry(window)
entry.pack()

start_button = tk.Button(window, text='Start', command=start_timer)
start_button.pack()

# Start the GUI main loop
window.mainloop()
