from tkinter import *


root = Tk()
root.title("Calculadora")

display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)

i=0


# ---------- FUNCTIONS ----------
def get_numbers(n):
    global i
    display.insert(i, n)
    i+=1

def get_operations(operator):
    global i
    leng_operator = len(operator)
    display.insert(i, operator)
    i+=leng_operator
    
def display_clear():
    display.delete(0, END)

def clear_one():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        display_clear()
        display.insert(0, display_new_state)
    else:
        display_clear()
        display.insert(0, 'ERROR')
        
def calculat():
    display_state = display.get()
    try:
        math_expression =  compile(display_state, 'app.py', 'eval')
        result = eval(math_expression)
        display_clear()
        display.insert(0,result)
    except:
        display_clear()
        display.insert(0,'ERROR')


# ---------- BUTTONS ----------
Button(root, text="1", command=lambda:get_numbers(1)).grid(row=2, column=0, sticky=W+E)
Button(root, text="2", command=lambda:get_numbers(2)).grid(row=2, column=1, sticky=W+E)
Button(root, text="3", command=lambda:get_numbers(3)).grid(row=2, column=2, sticky=W+E)

Button(root, text="4", command=lambda:get_numbers(4)).grid(row=3, column=0, sticky=W+E)
Button(root, text="5", command=lambda:get_numbers(5)).grid(row=3, column=1, sticky=W+E)
Button(root, text="6", command=lambda:get_numbers(6)).grid(row=3, column=2, sticky=W+E)

Button(root, text="7", command=lambda:get_numbers(7)).grid(row=4, column=0, sticky=W+E)
Button(root, text="8", command=lambda:get_numbers(8)).grid(row=4, column=1,sticky=W+E)
Button(root, text="9", command=lambda:get_numbers(9)).grid(row=4, column=2, sticky=W+E)

# ---------- BUTTONS second ----------
Button(root, text="AC", command=lambda:display_clear()).grid(row=5, column=0, sticky=W+E)
Button(root, text="0", command=lambda:get_numbers(0)).grid(row=5, column=1, sticky=W+E)
Button(root, text="%", command=lambda:get_operations("%")).grid(row=5, column=2, sticky=W+E)

Button(root, text="+", command=lambda:get_operations("+")).grid(row=2, column=3, sticky=W+E)
Button(root, text="-", command=lambda:get_operations("-")).grid(row=3, column=3, sticky=W+E)
Button(root, text="*", command=lambda:get_operations("*")).grid(row=4, column=3, sticky=W+E)
Button(root, text="/", command=lambda:get_operations("/")).grid(row=5, column=3, sticky=W+E)


# ---------- BUTTONS three ----------
Button(root, text="←", command=lambda:clear_one()).grid(row=2, column=4, sticky=W+E, columnspan=2)
Button(root, text="exp", command=lambda:get_operations("**")).grid(row=3, column=4, sticky=W+E)
Button(root, text="^2", command=lambda:get_operations("**2")).grid(row=3, column=5, sticky=W+E)
Button(root, text="(", command=lambda:get_operations("(")).grid(row=4, column=4, sticky=W+E)
Button(root, text=")", command=lambda:get_operations(")")).grid(row=4, column=5, sticky=W+E)
Button(root, text="=", command=lambda:calculat()).grid(row=5, column=4, sticky=W+E, columnspan=2)


#Button(root, text="1").grid()

root.mainloop()