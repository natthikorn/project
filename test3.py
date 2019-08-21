from tkinter import *

master = Tk()
master.title("Welcome to app")
master.configure(background="green")
photo1 = PhotoImage(file="333.png")
Label(master, image=photo1, bg="black") .grid(row=0, column=1, sticky=W)

Label(master, text='ราคา/หน่วย').grid(row=1)
Label(master, text='น้ำหนัก').grid(row=2)
Label(master, text='รวม').grid(row=3)
e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
Label(master, text='บาท/กิโล').grid(row=1, column=2)
Label(master, text='กิโล').grid(row=2, column=2)
Label(master, text='บาท').grid(row=3, column=2)

btn = Button(master, text="ยืนยัน").grid(row=4, column=2)
mainloop()