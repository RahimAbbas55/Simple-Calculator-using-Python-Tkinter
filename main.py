from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry( root , width = 35 , borderwidth = 5 )
e.grid( row = 0 , column = 1 , columnspan = 3 , padx = 10 , pady = 10)

def buttonClick( number ):
    curr = e.get()
    e.delete(0, END)
    e.insert ( 0 , str(curr) + str(number))
def button_clear():
    e.delete ( 0 , END)
def buttonPlus():
    first_num = e.get()
    global fnum
    fnum = int(first_num)
    e.delete(0, END)
    global math_exp
    math_exp = "plus"
def buttonMinus():
    first_num = e.get()
    global fnum
    fnum = int(first_num)
    e.delete(0, END)
    global math_exp
    math_exp = "minus"
def buttonMultiply():
    first_num = e.get()
    global fnum
    fnum = int(first_num)
    e.delete(0, END)
    global math_exp
    math_exp = "multiply"

def buttonDivide():
    first_num = e.get()
    global fnum
    fnum = int(first_num)
    e.delete(0, END)
    global math_exp
    math_exp = "divide"

def buttonEqual():
    second_number = e.get()
    e.delete( 0 , END )
    if math_exp == "plus":
        e.insert(0, fnum + int(second_number))
    elif math_exp == "minus":
        e.insert(0, fnum - int(second_number))
    elif math_exp == "multiply":
        e.insert(0, fnum * int(second_number))
    elif math_exp== "divide":
        e.insert(0, fnum / int(second_number))

#button declaration

button_1 = Button( root , text = "1" , padx = 40 , pady = 20 , command = lambda: buttonClick(1))
button_2 = Button( root , text = "2" , padx = 40 , pady = 20 , command = lambda: buttonClick(2))
button_3 = Button( root , text = "3" , padx = 40 , pady = 20 , command = lambda: buttonClick(3))
button_4 = Button( root , text = "4" , padx = 40 , pady = 20 , command = lambda: buttonClick(4))
button_5 = Button( root , text = "5" , padx = 40 , pady = 20 , command = lambda: buttonClick(5))
button_6 = Button( root , text = "6" , padx = 40 , pady = 20 , command = lambda: buttonClick(6))
button_7 = Button( root , text = "7" , padx = 40 , pady = 20 , command = lambda: buttonClick(7))
button_8 = Button( root , text = "8" , padx = 40 , pady = 20 , command = lambda: buttonClick(8))
button_9 = Button( root , text = "9" , padx = 40 , pady = 20 , command = lambda: buttonClick(9))
button_0 = Button( root , text = "0" , padx = 40 , pady = 20 , command = lambda: buttonClick(0))

button_equal =Button( root , text = "=" , padx = 40 , pady = 20 , command = buttonEqual)
button_plus = Button( root , text = "+" , padx = 40 , pady = 20 , command = buttonPlus)
button_minus = Button( root , text = "-" , padx = 40 , pady = 20 , command = buttonMinus)
button_multiply = Button( root , text = "*" , padx = 40 , pady = 20 , command = buttonMultiply)
button_divide = Button( root , text = "/" , padx = 40 , pady = 20 , command = buttonDivide)


button_clear = Button( root , text = "AC" , padx = 40 , pady = 20 , command = button_clear)

#Putting buttons on screen

button_1.grid( row = 3 , column = 0 )
button_2.grid( row = 3 , column = 1 )
button_3.grid( row = 3 , column = 2 )
#-----
button_4.grid( row = 2 , column = 0 )
button_5.grid( row = 2 , column = 1 )
button_6.grid( row = 2 , column = 2 )
#-----
button_7.grid( row = 1 , column = 0 )
button_8.grid( row = 1 , column = 1 )
button_9.grid( row = 1 , column = 2 )
#-----
button_0.grid( row = 4 , column = 1 )
#-----
button_plus.grid( row = 2 , column = 3 )
button_minus.grid( row = 2 , column = 4 )
button_divide.grid( row = 1 , column = 3 )
button_multiply.grid( row = 1 , column = 4 )
button_equal.grid( row = 3 , column = 3 )
button_clear.grid( row = 3 , column = 4 )

root.mainloop()