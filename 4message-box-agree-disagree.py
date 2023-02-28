

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root=tk.Tk()
root.geometry("400x400")
root.resizable(False,False)
root.title("CheckBox demo")

agreement=tk.StringVar()

def agreement_changed():
    tk.messagebox.showinfo(title='result',message=agreement.get())

ttk.Checkbutton(root,text='I agree',command=agreement_changed,variable=agreement,onvalue='your agreed', offvalue='disagree').pack()

root.mainloop()
