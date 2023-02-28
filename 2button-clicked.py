

from tkinter import *
window=Tk()
window.title("Welcome to Tkinter")
window.geometry("400x400")
window.config(bg="green")
lbl=Label(window,text="Hello")
lbl.grid(column=0,row=0)

def clicked():
    lbl.configure(text="button was clicked by bosss")

btn=Button(window,text="click me",command=clicked)
btn.grid(column=1,row=0)

window.mainloop()
