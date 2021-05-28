#Create the GUI Interface
# Python code for creating a GUI Tkinter Calculator
# import tkinter package
from tkinter import *
# globally declare the expression variable
expression = ""
# Function to update expression in the text entry box
def press(num):
# point out the global expression variable 
    global expression
# concatenation of string
    expression = expression + str(num)
# update the expression by using set method   
    value.set(expression)
# Function to evaluate the final expression
def equalpress():
# Try and except statement is used for handling the errors
    try:
        global expression
# eval function evaluate the expression        
        total = str(eval(expression))
        
        value.set(total)
# initialze the expression variable        
        expression = ""
# if error is generate then handle by the except block        
    except:
        value.set(" Enter corect number ")
        expression = ""
# Function to clear the contents      
def clear():
    global expression
    expression = ""
    value.set("")
# Driver code
if __name__ == "__main__":
# Create a GUI window
    gui = Tk()
# set the background colour of GUI window 
    gui.configure(background="light gray")
# set tittle of GUI window
    gui.title("Calculator")
# set the configuration of GUI window    
    gui.geometry("336x140")
# StringVar() is the variable class    
    value = StringVar()
# create the text entry box    
    expression_field = Entry(gui, textvariable=value)
# grid method is used for placing the widgets at respective positions    
    expression_field.grid(columnspan=4, ipadx=70)
    
    value.set('Enter your expression')
    button1 = Button(gui, text=' 1 ', fg='black', bg='white', 
        command=lambda: press(1), height=1, width=7) 
    button1.grid(row=2, column=0) 

    button2 = Button(gui, text=' 2 ', fg='black', bg='white', 
        command=lambda: press(2), height=1, width=7) 
    button2.grid(row=2, column=1) 

    button3 = Button(gui, text=' 3 ', fg='black', bg='white', 
        command=lambda: press(3), height=1, width=7) 
    button3.grid(row=2, column=2) 

    button4 = Button(gui, text=' 4 ', fg='black', bg='white', 
        command=lambda: press(4), height=1, width=7) 
    button4.grid(row=3, column=0) 

    button5 = Button(gui, text=' 5 ', fg='black', bg='white', 
        command=lambda: press(5), height=1, width=7) 
    button5.grid(row=3, column=1) 

    button6 = Button(gui, text=' 6 ', fg='black', bg='white', 
        command=lambda: press(6), height=1, width=7) 
    button6.grid(row=3, column=2) 

    button7 = Button(gui, text=' 7 ', fg='black', bg='white', 
        command=lambda: press(7), height=1, width=7) 
    button7.grid(row=4, column=0) 

    button8 = Button(gui, text=' 8 ', fg='black', bg='white', 
        command=lambda: press(8), height=1, width=7) 
    button8.grid(row=4, column=1) 

    button9 = Button(gui, text=' 9 ', fg='black', bg='white', 
        command=lambda: press(9), height=1, width=7) 
    button9.grid(row=4, column=2) 

    button0 = Button(gui, text=' 0 ', fg='black', bg='white', 
        command=lambda: press(0), height=1, width=7) 
    button0.grid(row=5, column=0) 

    plus = Button(gui, text=' + ', fg='gray', bg='white', 
        command=lambda: press("+"), height=1, width=7) 
    plus.grid(row=2, column=3) 

    minus = Button(gui, text=' - ', fg='gray', bg='white', 
        command=lambda: press("-"), height=1, width=7) 
    minus.grid(row=3, column=3) 

    multiply = Button(gui, text=' * ', fg='gray', bg='white', 
        command=lambda: press("*"), height=1, width=7) 
    multiply.grid(row=4, column=3) 

    divide = Button(gui, text=' / ', fg='gray', bg='white', 
        command=lambda: press("/"), height=1, width=7) 
    divide.grid(row=5, column=3) 

    equal = Button(gui, text=' = ', fg='gray', bg='white', 
        command=equalpress, height=1, width=7) 
    equal.grid(row=5, column=2) 

    clear = Button(gui, text='Clear', fg='gray', bg='white',
        command=clear, height=1, width=7) 
    clear.grid(row=5, column='1')

    # start the GUI 
    gui.mainloop()
    # Created by Adrian Josu @vexamd
    
 