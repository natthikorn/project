from tkinter import *


root = Tk()
root.title("Welcome to app")

root.option_add("*Font", "consoas 20")
photo = PhotoImage(file="333.png")
Button(root, text="แตงโม", fg="green",bd=10, image=photo, compound=LEFT, padx=20).pack()
Button(root, text="มะเขือ", fg="green",bd=10, image=photo, compound=LEFT, padx=20).pack()
Button(root, text="มะพร้าว", fg="green",bd=10, image=photo, compound=LEFT, padx=20).pack()





root.mainloop()