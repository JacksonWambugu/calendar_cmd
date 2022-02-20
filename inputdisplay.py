from distutils import command
import tkinter
from tkinter.tix import Tk
from tkinter.ttk import Entry
from turtle import width
root=Tk()
root.geometry("400x300")
def button():
    text=entry1.get()
    ht=int(text)
    print(ht)
    return None

entry1=Entry(root,width=20)
entry1.pack()

tkinter.Button(root,text="button",command=button).pack()

root.mainloop()