import tkinter
from tkinter import ttk
import funcgui

import functions
from tkinter import *

import tk as tk
fg = funcgui.Funcgui()
# fc = functions.Functions()
# #TODO 1 Zaprojektować przyjmowanie inputów do kalkulatora
# print("Welcome to basic calculator")
#
# is_on = True
# while is_on:
#     user_input_l1 = float(input("Please chose a number:   "))
#     user_input_dzialanie = input("Please chose an operation (* , / , + , - )")
#     user_input_l2 = float(input("Please chose second number "))
#
#     if user_input_dzialanie == "*":
#         print(f"Result is : {fc.multiplication(user_input_l1, user_input_l2)}")
#         is_on = fc.restart()
#     elif user_input_dzialanie == "/":
#         print(f"Result is : {fc.division(user_input_l1, user_input_l2)}")
#         is_on = fc.restart()
#     elif user_input_dzialanie == "+":
#         print(f"Result is : {fc.sum(user_input_l1, user_input_l2)}")
#         is_on = fc.restart()
#     elif user_input_dzialanie == "-":
#         print(f"Result is : {fc.diffrence(user_input_l1, user_input_l2)}")
#         is_on = fc.restart()
#     else:
#         print("You've chosen a wrong operation sign")


#todo 3 Zaprojektować graficzny szatę kalkulatora za pomocą tkinter

root = tkinter.Tk()
root.title("Calculator")
root.config(padx=100, pady=20)

filed_text = ""
entry = Entry(width=11, font=("Times", "45", "bold"))
entry.grid(column=0, row=0, columnspan=4)
expression = ""
# trzeba tu napisac ze bierze "score" z funkcji gui oraz ze ma pisac od prawej na początku niech wyświetla zero
# TODO oraz następnie, żeby dodawal liczbę za kazdym wcisnieciem klawisza

buttonC = Button(width=10, height=5, text="C")
buttonC.grid(column=0, row=1)

button_mnozenie = Button(width=10, height=5, text="X")
button_mnozenie.grid(column=1, row=1)

button_dzielenie = Button(width=10, height=5, text="/")
button_dzielenie.grid(column=2, row=1)

button_dodawanie = Button(width=10, height=11, text="+")
button_dodawanie.grid(column=3, row=1, rowspan=2)

button_odejmowanie = Button(width=10, height=5, text="-")
button_odejmowanie.grid(column=3, row=3)

button_procent = Button(width=10, height=5, text="%")
button_procent.grid(column=3, row=4)

button1 = Button(width=10, height=5, text="1", command=lambda : entry.insert(0, 1))
button1.grid(column=0, row=2)

button2 = Button(width=10, height=5, text="2", command=lambda : entry.insert(0, 2))
button2.grid(column=1, row=2)

button3 = Button(width=10, height=5, text="3", command=lambda : entry.insert(0, 3))
button3.grid(column=2, row=2)

button4 = Button(width=10, height=5, text="4", command=lambda : entry.insert(0, 4))
button4.grid(column=0, row=3)

button5 = Button(width=10, height=5, text="5", command=lambda : entry.insert(0, 5))
button5.grid(column=1, row=3)

button6 = Button(width=10, height=5, text="6", command=lambda : entry.insert(0, 6))
button6.grid(column=2, row=3)

button7 = Button(width=10, height=5, text="7", command=lambda : entry.insert(0, 7))
button7.grid(column=0, row=4)

button8 = Button(width=10, height=5, text="8", command=lambda : entry.insert(0, 8))
button8.grid(column=1, row=4)

button9 = Button(width=10, height=5, text="9", command=lambda : entry.insert(0, 9))
button9.grid(column=2, row=4)

button0 = Button(width=10, height=5, text="0", command=lambda : entry.insert(0, 0))
button0.grid(column=0, row=5)

buttonP = Button(width=10, height=5, text=".", command=lambda : entry.insert(0, "."))
buttonP.grid(column=1, row=5)

buttonR = Button(width=21, height=5, text="=")
buttonR.grid(column=2, row=5, columnspan=3)




root.mainloop()

#todo 4 Dodać funkcjonalność + szatę graficzną