from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
from datetime import datetime

def writecsv(datalist):
    with open('data.csv', 'a', encoding='utf-8', newline='') as file:
        fw = csv.writer(file)
        fw.writerow(datalist)

def readcsv():
    with open('data.csv', encoding='utf-8', newline='') as file:
        fr = csv.reader(file)
        data = list(fr)
    return data

GUI = Tk()
GUI.title('โปรแกรมคำนวณเปอร์เซ็นต์แบตเตอรี่')
GUI.geometry('500x400')

L1 = Label(GUI, text='คำนวณเปอร์เซ็นต์แบตเตอรี่', font=('Cordia New', 30), fg='green')
L1.place(x=30, y=20)

min_volt = StringVar()
L2 = Label(GUI, text='โวลต์ต่ำสุด', font=('Cordia New', 24), fg='green')
L2.place(x=30, y=80)
E2 = ttk.Entry(textvariable=min_volt)
E2.place(x=150, y=91)

max_volt = StringVar()
L3 = Label(GUI, text='โวลต์สูงสุด', font=('Cordia New', 24), fg='green')
L3.place(x=30, y=120)
E3 = ttk.Entry(textvariable=max_volt)
E3.place(x=150, y=131)

current_volt = StringVar()
L4 = Label(GUI, text='โวลต์ตอนนี้', font=('Cordia New', 24), fg='green')
L4.place(x=30, y=160)
E4 = ttk.Entry(textvariable=current_volt)
E4.place(x=150, y=171)

def SaveData():
    cal = ((float(current_volt.get()) - float(min_volt.get())) / (float(max_volt.get()) - float(min_volt.get()))) * 100
    cal = str(round(cal, 2))
    t = datetime.now().strftime('%Y/%m/%d, %H:%M:%S')
    text1 = f'ตอนนี้มี {cal}%'
    print_text = text1 + '\nบันทึกเรียบร้อยแล้ว'
    text2 = [t, text1]
    writecsv(text2)
    messagebox.showinfo('สถานะแบตเตอรี่', print_text)
    min_volt.set('')
    max_volt.set('')
    current_volt.set('')

FB1 = Frame(GUI)
FB1.place(x=158, y=220)
B2 = ttk.Button(FB1, text='คำนวณ และบันทึก', command=SaveData)
B2.pack(ipadx=20, ipady=20)

FB2 = Frame(GUI)
FB2.place(x=158, y=220)



GUI.mainloop()
