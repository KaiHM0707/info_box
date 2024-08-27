from tkinter import *
from time import strftime

def time():
    string = strftime("%H:%M:%S %p")
    time_label.config(text=string)
    time_label.after(1000, time)




scr = Tk()
scr.title = "Clock"

time_label = Label(scr, fg="white", bg="purple", font=("Times", 45, "bold"))
time_label.pack()

time()


scr.mainloop()