

from tkinter import *
master=Tk()
master.geometry("400x400")
var1=IntVar()
Checkbutton(master,text='male',variable=var1).grid(row=0,stick=W)
var2=IntVar()
Checkbutton(master,text='female',variable=var2).grid(row=1,stick=W)

var3=IntVar()
Checkbutton(master,text='cse',variable=var3).grid(row=2,stick=W)


mainloop()
