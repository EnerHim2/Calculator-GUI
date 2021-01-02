from tkinter import *
import tkinter as tk


expression = ""

def press(num):
    global expression

    expression += str(num)
    equation.set(expression)

def equal():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression=""
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression

    equation.set("")
    expression = ""        

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Calculator")
    equation = StringVar()

    expression_field = Entry(root, textvariable=equation) 
    expression_field.grid(columnspan=4, ipadx=70) 

    one = tk.Button(root , text="1", width=8, height=4, command=lambda:press(1)).grid(row=1, column=0)
    two = tk.Button(root , text="2", width=8, height=4, command=lambda:press(2)).grid(row=1, column=1)
    three = tk.Button(root , text="3", width=8, height=4, command=lambda:press(3)).grid(row=1, column=2)
    four = tk.Button(root , text="4", width=8, height=4, command=lambda:press(4)).grid(row=2, column=0)
    five = tk.Button(root , text="5", width=8, height=4, command=lambda:press(5)).grid(row=2, column=1)
    six = tk.Button(root , text="6", width=8, height=4, command=lambda:press(6)).grid(row=2, column=2)
    seven = tk.Button(root , text="7", width=8, height=4, command=lambda:press(7)).grid(row=3, column=0)
    eight = tk.Button(root , text="8", width=8, height=4, command=lambda:press(8)).grid(row=3, column=1)
    nine = tk.Button(root , text="9", width=8, height=4, command=lambda:press(9)).grid(row=3, column=2)
    zero = tk.Button(root , text="0", width=8, height=4, command=lambda:press(0)).grid(row=4, column=1)
    add = tk.Button(root , text="+", width=8, height=4, command=lambda:press("+")).grid(row=1, column=3)
    minus = tk.Button(root , text="-", width=8, height=4, command=lambda:press("-")).grid(row=2, column=3)
    divide = tk.Button(root , text="/", width=8, height=4, command=lambda:press("/")).grid(row=3, column=3)
    multiply = tk.Button(root , text="*", width=8, height=4, command=lambda:press("*")).grid(row=4, column=3)
    equal = tk.Button(root , text="=", width=8, height=4, command=equal).grid(row=4, column=2)
    clear = tk.Button(root , text="C", width=8, height=4, command=clear).grid(row=4, column=0)

root.mainloop()
