
from tkinter import *

window = Tk()
window.geometry('500x500')

# adding inputs

#entry box
e = Entry(window , width = 56, borderwidth= 5)
e.place(x = 0,y = 0)


#btn

def click(num):
    result = e.get()
    e.delete(0,END)
    e.insert(0 , str(result) + str(num))

b = Button(window , text = '1' , width = 12 , command = lambda:click(1))
b.place(x = 10,y = 50)

b = Button(window , text = '2' , width = 12 , command = lambda:click(2))
b.place(x = 90,y = 50)

b = Button(window , text = '3' , width = 12 , command = lambda:click(3))
b.place(x = 170,y = 50)

def add():
    n1 = e.get()
    global math
    math = "addition"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window , text = '+' , width = 12 , command = add)
b.place(x = 250,y = 50)

b = Button(window , text = '4' , width = 12 , command = lambda:click(4))
b.place(x = 10,y = 100)

b = Button(window , text = '5' , width = 12 , command = lambda:click(5))
b.place(x = 90,y = 100)

b = Button(window , text = '6' , width = 12 , command = lambda:click(6))
b.place(x = 170,y = 100)

def sub():
    n1 = e.get()
    global math
    math = "substraction"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window , text = '-' , width = 12 , command = sub)
b.place(x = 250,y = 100)

b = Button(window , text = '7' , width = 12)
b.place(x = 10,y = 150)

b = Button(window , text = '8' , width = 12 , command = lambda:click(8))
b.place(x = 90,y = 150)

b = Button(window , text = '9' , width = 12 , command = lambda:click(9))
b.place(x = 170,y = 150)

def mult():
    n1 = e.get()
    global math
    math = "multiplication"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window , text = '*' , width = 12 , command = mult)
b.place(x = 250,y = 150)

def clear():
    e.delete(0 , END)
b = Button(window , text = 'clear' , width = 12 , command = clear)
b.place(x = 10,y = 200)

b = Button(window , text = '0' , width = 12 , command = lambda:click(0))
b.place(x = 90,y = 200)

def equal():
    n2 = e.get()
    e.delete(0,END)
    if math == "addition":
        e.insert(0,i + int(n2))
    elif math == "substraction":
        e.insert(0,i - int(n2))
    elif math == "multiplication":
        e.insert(0,i * int(n2))
    elif math == "division":
        e.insert(0,i / int(n2))

b = Button(window , text = '=' , width = 12 , command = equal)
b.place(x = 170,y = 200)

def div():
    n1 = e.get()
    global math
    math = "division"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window , text = '/' , width = 12 , command = div)
b.place(x = 250,y = 200)

mainloop()
