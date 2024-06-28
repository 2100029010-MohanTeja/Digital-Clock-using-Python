import tkinter as ui
import time

window = ui.Tk()

def update_clock():
    hours = time.strftime("%I")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    am_or_pm = time.strftime("%p")
    current_time = hours + ":" + minutes + ":" + seconds + " " + am_or_pm
    
    date = time.strftime("%d")
    month = time.strftime("%B")
    year = time.strftime("%Y")
    current_date = date + " " + month + " " + year
    
    time_text = current_time + "\n" + current_date
    digital_clock_lbl.config(text=time_text)
    digital_clock_lbl.after(1000, update_clock)

digital_clock_lbl = ui.Label(window, text="00:00:00", font="Helvetica 48 bold")
digital_clock_lbl.pack()

update_clock()

window.mainloop()
