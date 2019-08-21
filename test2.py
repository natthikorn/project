from tkinter import *
from tkinter.ttk import *
window = Tk()
window.title("Welcome to app")

selected = IntVar()
rad1 = Radiobutton(window, text='แตงโม', value=1, variable=selected)
rad2 = Radiobutton(window, text='มะเขือ', value=2, variable=selected)
rad3 = Radiobutton(window, text='มะพร้าว', value=3, variable=selected)

def clicked():
    print(selected.get())

btn = Button(window, text="ยืนยัน", command=clicked)
rad1.grid(column=0, row=0)
rad2.grid(column=0, row=1)
rad3.grid(column=0, row=2)
btn.grid(column=0, row=3)

window.mainloop()