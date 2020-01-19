"""
Simple Calculator
By Daniel Ha 
Contact: bb13112001@gmail.com
"""
from tkinter import *
from math import sqrt

master = Tk()
master.title("Calculator")
 
e = Entry(master, width = 40, borderwidth = 3)
e.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5)

def show_value(num): 
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))
    return

def clear():
    e.delete(0,END)
    return

def add():
    global status
    status = 'addition'
    fnum = e.get()
    global num1
    num1 = int(fnum)
    e.delete(0, END)
    return

def sub():    
    global status
    status = 'subtraction'
    fnum = e.get()
    global num1
    num1 = int(fnum)
    e.delete(0, END)
    return

def div():
    global status
    status = 'division'
    fnum = e.get()
    global num1
    num1 = int(fnum)
    e.delete(0, END)
    return

def multiply():
    global status
    status = 'multiply'
    fnum = e.get()
    global num1
    num1 = int(fnum)
    e.delete(0, END)
    return

def square_root():
    global status
    status = 'square_root'
    fnum = e.get()
    global num1
    num1 = int(fnum)
    e.delete(0, END)
    return

def power():
    global status
    status = 'power'
    fnum = e.get()
    global num1
    num1 = int(fnum)
    e.delete(0, END)
    return

def equal():
    if status == 'addition':
        num2 = e.get()
        e.delete(0, END)
        e.insert(0, num1 + int(num2))
    elif status == 'subtraction':
        num2 = e.get()
        e.delete(0, END)
        e.insert(0, num1 - int(num2))
    elif status == 'division':
        num2 = e.get()
        e.delete(0, END)
        e.insert(0, num1 / int(num2))
    elif status == 'multiply':
        num2 = e.get()
        e.delete(0, END)
        e.insert(0, num1 * int(num2))
    elif status == 'square_root':
        e.insert(0, sqrt(num1))
    elif status == 'power':
        num2 = e.get()
        e.delete(0, END)
        e.insert(0, num1 ** int(num2))
    return
    


button1 = Button(master, text = '1',padx = 25, pady = 10, command = lambda :show_value(1))
button2 = Button(master, text = '2',padx = 25, pady = 10, command = lambda :show_value(2))
button3 = Button(master, text = '3',padx = 25, pady = 10, command = lambda :show_value(3))
button4 = Button(master, text = '4',padx = 25, pady = 10, command = lambda :show_value(4))
button5 = Button(master, text = '5',padx = 25, pady = 10, command = lambda :show_value(5))
button6 = Button(master, text = '6',padx = 25, pady = 10, command = lambda :show_value(6))
button7 = Button(master, text = '7',padx = 25, pady = 10, command = lambda :show_value(7))
button8 = Button(master, text = '8',padx = 25, pady = 10, command = lambda :show_value(8))
button9 = Button(master, text = '9',padx = 25, pady = 10, command = lambda :show_value(9))
button0 = Button(master, text = '0',padx = 25, pady = 10, command = lambda :show_value(0))

button_equal = Button(master, text = '=', padx = 90, pady = 10, command = equal)
button_clear = Button(master, text = 'C', padx = 25, pady = 10, command = clear)
button_add = Button(master, text = '+', padx = 25, pady = 10, command = add)
button_subtract = Button(master, text = '-', padx = 25, pady = 10, command = sub)
button_divide = Button(master, text = '/', padx = 25, pady = 10, command = div)
button_multiply = Button(master, text = '*', padx = 25, pady = 10, command = multiply)
button_square_root = Button(master, text = '√', padx = 25, pady = 10, command = square_root)
button_power = Button(master, text = '^', padx = 25, pady = 10, command = power)


button1.grid(row = 4, column = 0)
button2.grid(row = 4, column = 1)
button3.grid(row = 4, column = 2)

button4.grid(row = 3, column = 0)
button5.grid(row = 3, column = 1)
button6.grid(row = 3, column = 2)

button7.grid(row = 2, column = 0)
button8.grid(row = 2, column = 1)
button9.grid(row = 2, column = 2)

button0.grid(row = 5, column = 0)
button_equal.grid(row = 5, column = 1, columnspan = 3)
button_clear.grid(row = 1, column = 0)
button_add.grid(row = 2, column = 3)
button_subtract.grid(row = 1, column = 3)
button_divide.grid(row = 1, column = 1)
button_multiply.grid(row = 1, column = 2)
button_square_root.grid(row = 3, column = 3)
button_power.grid(row = 4, column = 3)


master.mainloop()