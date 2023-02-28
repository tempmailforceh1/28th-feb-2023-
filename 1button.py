

from tkinter import *
window=Tk()
window.title("Welcome to Tkinter")
window.geometry("400x400")
window.config(bg="sky blue")
lbl=Label(window,text="Hello")
lbl.grid(column=0,row=0)
btn=Button(window,text="Click me")
btn.grid(column=0,row=1)
window.mainloop()
