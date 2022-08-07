from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Digital Clock")

def time():
    string = strftime('%H:%M:%S')
    Label.config(text=string) 
    Label.after(1000,time)

Label = Label(root, font=("ds-digital",80),background = "black",foreground="cyan")
Label.pack(anchor='center')

time()
mainloop()
