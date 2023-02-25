from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('โปรแกรมคำนวณเปอร์เซ็นต์แบตเตอรี่')
GUI.geometry('500x400')

L1 = Label(GUI, text='คำนวณเปอร์เซ็นต์แบตเตอรี่', font=('Cordia New', 30), fg='green')
L1.place(x=30, y=20)

L2 = Label(GUI, text='โวลต์ต่ำสุด', font=('Cordia New', 24), fg='green')
L2.place(x=30, y=80)
E2 = ttk.Entry()
E2.place(x=150, y=91)

L3 = Label(GUI, text='โวลต์สูงสุด', font=('Cordia New', 24), fg='green')
L3.place(x=30, y=120)
E3 = ttk.Entry()
E3.place(x=150, y=131)

L4 = Label(GUI, text='โวลต์ตอนนี้', font=('Cordia New', 24), fg='green')
L4.place(x=30, y=160)
E4 = ttk.Entry()
E4.place(x=150, y=171)

def Button2():
    text = 'ตอนนี้มี __%'
    messagebox.showinfo('สถานะแบตเตอรี่', text)

FB1 = Frame(GUI)
FB1.place(x=158, y=220)
B2 = ttk.Button(FB1, text='คำนวณเปอร์เซ็นต์', command=Button2)
B2.pack(ipadx=20, ipady=20)

GUI.mainloop()