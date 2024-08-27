from tkinter import *
from tkinter import messagebox

def show_info():
    messagebox.showinfo("Oops", "there was an unknown error")

scr = Tk()
scr.title="info_box"

but1 = Button(scr, text="show info", command=show_info)
but1.pack()

scr.mainloop()


