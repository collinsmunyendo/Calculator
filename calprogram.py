from tkinter import *
import parser

root = Tk()
root.title("Calculator")

# get user input and place it in the text field
i = 0
def get_variable(num):
    global i
    display.insert(i, num)
    num += 1

def clear_all():
    display.delete(0, END)

def back_space():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)

    else:
        clear_all()
        display.insert(0, "Error")

# adding the input fields
display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)

# adding buttons to the calculator
Button(root, text="1", command=lambda : get_variable(1)).grid(row=2, column=0)
Button(root, text="2", command=lambda : get_variable(2)).grid(row=2, column=1)
Button(root, text="3", command=lambda : get_variable(3)).grid(row=2, column=2)

Button(root, text="4", command=lambda : get_variable(4)).grid(row=3, column=0)
Button(root, text="5", command=lambda : get_variable(5)).grid(row=3, column=1)
Button(root, text="6", command=lambda : get_variable(6)).grid(row=3, column=2)

Button(root, text="7", command=lambda : get_variable(7)).grid(row=4, column=0)
Button(root, text="8", command=lambda : get_variable(8)).grid(row=4, column=1)
Button(root, text="9", command=lambda : get_variable(9)).grid(row=4, column=2)

# adding other buttons to the calculator
Button(root, text="AC", command=lambda : clear_all()).grid(row=5, column=0)
Button(root, text="0", command=lambda : get_variable(0)).grid(row=5, column=1)
Button(root, text="=").grid(row=5, column=2)

Button(root, text="+").grid(row=2, column=3)
Button(root, text="-").grid(row=3, column=3)
Button(root, text="*").grid(row=4, column=3)
Button(root, text="/").grid(row=5, column=3)

# adding new operations
Button(root, text="pi").grid(row=2, column=4)
Button(root, text="%").grid(row=3, column=4)
Button(root, text="(").grid(row=4, column=4)
Button(root, text="exp").grid(row=5, column=4)

Button(root, text="<-", command=lambda : back_space()).grid(row=2, column=5)
Button(root, text="x!").grid(row=3, column=5)
Button(root, text=")").grid(row=4, column=5)
Button(root, text="^2").grid(row=5, column=5)

root.mainloop()