from tkinter import *

root = Tk()
root.title("Welcome to app")

photo = PhotoImage(file="333.png")
label = Label(root, image=photo)
label.pack()

root.mainloop()