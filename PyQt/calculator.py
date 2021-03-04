'''
Version: 3.7.8
Libraries: 
- PyQt5 (pip3 install pyqt5)
- Sys (default with python)
Tested on macOS 11.1 Big Sur
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import Qt
from PyQt5 import QtCore
from PyQt5.QtCore import *


equation = ""
equation2 = ""
corners = 0


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

    def keyPressEvent(self, event):
        global equation, equation2
        if event.text() == "=" or event.key() == 16777220:
            try:
                equation = str(round(eval(equation), 5))
                lbl.setText(equation)
            except Exception as e:
                lbl.setText("ERROR")
                equation = ""
                equation2 = ""
        elif event.key() == 81:
            sys.exit()
        elif event.key() == 67:
            equation = ""
            equation2 = ""
            lbl.setText("0")
        else:
            equation = equation + str(event.text())
            equation2 = equation
            equation2 = equation2.replace("*", "×")
            equation2 = equation2.replace("/", "÷")
            lbl.setText(equation2)

    def update_equation():
        global equation, equation2
        equation2 = equation
        equation2 = equation2.replace("*", "×")
        equation2 = equation2.replace("/", "÷")
        lbl.setText(equation2)


app = QApplication(sys.argv)
window = MainWindow()
window.setWindowTitle("Calculator")
window.setFixedSize(500, 600)  # 450, 550


def button_press(value):
    global equation, equation2
    if value == "C":
        lbl.setText("0")
        equation = ""
        equation2 = ""
    elif value == "=":
        try:
            equation = str(round(eval(equation), 5))
            lbl.setText(equation)
        except Exception as e:
            lbl.setText("ERROR")
    else:
        equation = equation + str(value)
        equation2 = equation
        equation2 = equation2.replace("*", "×")
        equation2 = equation2.replace("/", "÷")
        lbl.setText(equation2)


def quit():
    sys.exit()


def create_button(text, row, column, color, width, height, func_value):
    btn = QPushButton(text=text)
    btn.setFixedSize(width, height)
    btn.setStyleSheet(f"""
        background-color: {color};
        color: white;
        border-radius: {corners}px;
    """)
    btn.setFont(QFont("Helvetica", 25))
    btn.clicked.connect(lambda: button_press(func_value))
    layout.addWidget(btn, row, column)


frm = QFrame(window)
layout = QGridLayout()
frm.setLayout(layout)


def get_corners(value):
    global corners
    corners = int(value)
    # print(frm.children())
    for widget in frm.children():
        if widget != quitbtn:
            try:
                widget.setStyleSheet(
                    f"{widget.styleSheet()}\nborder-radius: {corners}px;")
            except Exception as e:
                pass
    # print(value)


slider = QSlider(Qt.Vertical, window)
slider.resize(30, 300)
slider.setRange(0, 50)
slider.setPageStep(5)
slider.valueChanged.connect(get_corners)
slider.setTickInterval(100)
layout.addWidget(slider, 0, 5, 6, 1)


# Orange: 255, 165, 0
# Gray: 128, 128, 128
# Light Gray: 166, 166, 166
buttons = {
    "0": (4, 0),
    "1": (3, 0),
    "2": (3, 1),
    "3": (3, 2),
    "4": (2, 0),
    "5": (2, 1),
    "6": (2, 2),
    "7": (1, 0),
    "8": (1, 1),
    "9": (1, 2),
}
for button, pos in buttons.items():
    create_button(text=button, row=pos[0], color="rgb(128, 128, 128)",
                  column=pos[1], width=100, height=100, func_value=button)


create_button("C", 4, 2, "rgb(166, 166, 166)", 100, 100, "C")
create_button(".", 4, 1, "rgb(166, 166, 166)", 100, 100, ".")
create_button("÷", 0, 3, "rgb(255, 165, 0)", 100, 100, "/")
create_button("×", 1, 3, "rgb(255, 165, 0)", 100, 100, "*")
create_button("+", 2, 3, "rgb(255, 165, 0)", 100, 100, "+")
create_button("-", 3, 3, "rgb(255, 165, 0)", 100, 100, "-")
create_button("=", 4, 3, "rgb(255, 165, 0)", 100, 100, "=")

quitbtn = QPushButton(text="QUIT")
quitbtn.setFixedSize(100, 100)
quitbtn.setStyleSheet("""
    border-radius: 50px;
    background-color: rgb(225, 0, 0);
    color: white;
""")
quitbtn.setFont(QFont("Helvetica", 20))
quitbtn.clicked.connect(quit)
layout.addWidget(quitbtn, 0, 0)


lbl = QLabel(text="0", parent=window)
lbl.setFixedSize(205, 100)
lbl.setStyleSheet(f"""
    border-radius: {corners}px;
    background-color: black;
    color: white;
""")
lbl.setAlignment(QtCore.Qt.AlignCenter)
lbl.setFont(QFont("Helvetica", 25))
layout.addWidget(lbl, 0, 1, 1, 2)


# window.setLayout(layout)
window.show()
sys.exit(app.exec_())
