'''
Version: 3.8.7
Libraries: 
- tkinter (default with python)
- tkmacosx (pip3 install tkmacosx)
- sys (default with python)

Tested on macOS 11.1 Big Sur
'''

from tkinter import *
from tkmacosx import Button, CircleButton
import sys


window = Tk()
window.title("Calculator")
window.rowconfigure([0, 1, 2, 3, 4, 5], weight=1, minsize=100)
window.columnconfigure([0, 1, 2, 3, 4, 5], weight=1, minsize=100)
window.geometry("410x510")


equation = ""
equation2 = ""
button_clicked = ""


def button_press(value):
    global equation
    global equation2
    equation = equation + str(value)
    equation2 = equation
    equation2 = equation2.replace("*", "×")
    equation2 = equation2.replace("/", "÷")
    label["text"] = equation2


def equals():
    global equation
    try:  # Trying for an error
        answer = round((eval(equation)), 8)
    except:  # Excepting the error
        label["text"] = "ERROR"
    label["text"] = answer


def clear():
    global equation
    label["text"] = "0"
    equation = ""


def type(event):
    global equation
    global equation2
    global button_clicked
    button_clicked = event.char
    if button_clicked == "=":
        try:  # Trying for an error
            answer = round(eval(equation), 8)
            label["text"] = answer
        except:  # Excepting the error
            label["text"] = "ERROR"
    elif button_clicked == "c":
        label["text"] = 0
        equation = ""
        equation2 = ""
    elif button_clicked == "q":
        window.destroy()
        sys.exit()
    else:
        equation = equation + str(button_clicked)
        equation2 = str(equation)
        equation2 = equation2.replace("*", "×")
        equation2 = equation2.replace("/", "÷")
        label["text"] = equation2


def enter(event):
    global equation, equation2
    try:
        answer = round(eval(equation), 8)
        label["text"] = answer
    except:
        label["text"] = "ERROR"


window.bind("<Return>", enter)


def quit():
    window.destroy()
    sys.exit()


window.bind("<Key>", type)

btn0 = Button(text="0", fg="white", bg="gray", borderless=True,
              command=lambda: button_press(0), font=(None, 25))
btn1 = Button(text="1", fg="white", bg="gray", borderless=True,
              command=lambda: button_press(1), font=(None, 25))
btn2 = Button(text="2", fg="white", bg="gray", borderless=True,
              command=lambda: button_press(2), font=(None, 25))
btn3 = Button(text="3", fg="white", bg="gray", borderless=True,
              command=lambda: button_press(3), font=(None, 25))
btn4 = Button(text="4", fg="white", bg="gray", borderless=True,
              command=lambda: button_press(4), font=(None, 25))
btn5 = Button(text="5", fg="white", bg="gray", borderless=True,
              command=lambda: button_press(5), font=(None, 25))
btn6 = Button(text="6", fg="white", bg="gray", borderless=True,
              command=lambda: button_press(6), font=(None, 25))
btn7 = Button(text="7", fg="white", bg="gray", borderless=True,
              command=lambda: button_press(7), font=(None, 25))
btn8 = Button(text="8", fg="white", bg="gray", borderless=True,
              command=lambda: button_press(8), font=(None, 25))
btn9 = Button(text="9", fg="white", bg="gray", borderless=True,
              command=lambda: button_press(9), font=(None, 25))
quit = CircleButton(text="QUIT", fg="white", bg="red",
                    borderless=True, command=quit, font=(None, 20))


clear = Button(text="C", fg="white", bg="gray65",
               borderless=True, command=clear, font=(None, 25))
decimal = Button(text=".", fg="white", bg="gray65", borderless=True,
                 command=lambda: button_press("."), font=(None, 25))


divide = Button(text="÷", fg="white", bg="orange", borderless=True,
                command=lambda: button_press("/"), font=(None, 25))
multiply = Button(text="×", fg="white", bg="orange", borderless=True,
                  command=lambda: button_press("*"), font=(None, 25))
add = Button(text="+", fg="white", bg="orange", borderless=True,
             command=lambda: button_press("+"), font=(None, 25))
subtract = Button(text="-", fg="white", bg="orange", borderless=True,
                  command=lambda: button_press("-"), font=(None, 25))
equals = Button(text="=", fg="white", bg="orange",
                borderless=True, command=equals, font=(None, 25))


label = Label(text="0", fg="white", bg="black", font=(None, 25))


btn1.grid(row=3, column=0, sticky="nsew")
btn2.grid(row=3, column=1, sticky="nsew")
btn3.grid(row=3, column=2, sticky="nsew")

btn4.grid(row=2, column=0, sticky="nsew")
btn5.grid(row=2, column=1, sticky="nsew")
btn6.grid(row=2, column=2, sticky="nsew")

btn7.grid(row=1, column=0, sticky="nsew")
btn8.grid(row=1, column=1, sticky="nsew")
btn9.grid(row=1, column=2, sticky="nsew")

btn0.grid(row=4, column=0, sticky="nsew")
decimal.grid(row=4, column=1, sticky="nsew")
clear.grid(row=4, column=2, sticky="nsew")


divide.grid(row=0, column=3, sticky="nsew")
multiply.grid(row=1, column=3, sticky="nsew")
add.grid(row=2, column=3, sticky="nsew")
subtract.grid(row=3, column=3, sticky="nsew")
equals.grid(row=4, column=3, sticky="nsew")

label.grid(row=0, column=1, columnspan=2, sticky="nsew")
quit.grid(row=0, column=0, sticky="nsew")

window.mainloop()
