from tkinter import *

import calendar
from tkinter import font


year = int(input("Enter your prefffered year"))

text =calendar.calendar(year)
root=Tk()
root.geometry("550x600")
root.title("CALENDAR")
label1=Label(root,text="CALENDAR",bg='#00ffcc',font=("times",28,'bold'))
label2=Label(root,text="Enter your Preffered Year",bg='#00ffcc',font=("times",28,'bold'))

label1.grid(row=1,column=1)
root.config(background="#ff00ff")
l1=Label(root,text=text,font="Consolas 10")

l1.grid(row=2,column=1,padx=15)
root.mainloop()