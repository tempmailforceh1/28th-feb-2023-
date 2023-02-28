import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

#root window

root=tk.Tk()

root.geometry('300x300')
root.resizable(False,False)

root.title('Radio Button Demo')

def show_selected_size():
    showinfo(title='Result',
    message=selected_size.get())

selected_size=tk.StringVar()
sizes=(('small','S'),('medium','M'),
       ('large','L'),('Extra large','XL'),
       ('Extra Extralarge','XXL'))

#label

label=ttk.Label(text="whats your tshirt size")
label.pack(fill='x',padx=5,pady=5)

#radio buttons

for size in sizes:

    r=ttk.Radiobutton(root,text=size[0],value=size[1],variable=selected_size)
    r.pack(fill='x',padx=5,pady=5)


#button

button=ttk.Button(root,text="Get Selected size",command=show_selected_size)

button.pack(fill='x',padx=5,pady=5)

root.mainloop()










