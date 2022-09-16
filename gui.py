from tkinter import *
import tkinter
import math


class Gui:

    def __int__(self):
        root = tkinter.Tk()
        root.title("Calculator")
        root.config(padx=100, pady=20)

        self.main_entry = Entry(width=11, font=("Times", "45", "bold"))
        self.main_entry.grid(column=0, row=0, columnspan=4)

        buttonC = Button(width=10, height=5, text="C", command=self.delete)
        buttonC.grid(column=0, row=1)

        button_mnozenie = Button(width=10, height=5, text="X", command=self.multi)
        button_mnozenie.grid(column=1, row=1)

        button_dzielenie = Button(width=10, height=5, text="/")
        button_dzielenie.grid(column=2, row=1)

        button_dodawanie = Button(width=10, height=11, text="+")
        button_dodawanie.grid(column=3, row=1, rowspan=2)

        button_odejmowanie = Button(width=10, height=5,)
        button_odejmowanie.grid(column=3, row=3)

        button_procent = Button(width=10, height=5, text="%")
        button_procent.grid(column=3, row=4)

        button1 = Button(width=10, height=5, text="1",
                         command=lambda : self.main_entry.insert(self.lenght_of_entry(), 1))
        button1.grid(column=0, row=2)

        button2 = Button(width=10, height=5, text="2",
                         command=lambda :self.main_entry.insert(self.lenght_of_entry(), 2))
        button2.grid(column=1, row=2)

        button3 = Button(width=10, height=5, text="3",
                         command=lambda : self.main_entry.insert(self.lenght_of_entry(), 3))
        button3.grid(column=2, row=2)

        button4 = Button(width=10, height=5, text="4",
                         command=lambda : self.main_entry.insert(self.lenght_of_entry(), 4))
        button4.grid(column=0, row=3)

        button5 = Button(width=10, height=5, text="5",
                         command=lambda : self.main_entry.insert(self.lenght_of_entry(), 5))
        button5.grid(column=1, row=3)

        button6 = Button(width=10, height=5, text="6",
                         command=lambda : self.main_entry.insert(self.lenght_of_entry(), 6))
        button6.grid(column=2, row=3)

        button7 = Button(width=10, height=5, text="7",
                         command=lambda : self.main_entry.insert(self.lenght_of_entry(), 7))
        button7.grid(column=0, row=4)

        button8 = Button(width=10, height=5, text="8",
                         command=lambda : self.main_entry.insert(self.lenght_of_entry(), 8))
        button8.grid(column=1, row=4)

        button9 = Button(width=10, height=5, text="9",
                         command=lambda : self.main_entry.insert(self.lenght_of_entry(), 9))
        button9.grid(column=2, row=4)

        button0 = Button(width=10, height=5, text="0",
                         command=lambda : self.main_entry.insert(self.lenght_of_entry(), 0))
        button0.grid(column=0, row=5)

        buttonP = Button(width=10, height=5, text=".",
                         command=lambda : self.main_entry.insert(self.lenght_of_entry(), "."))
        buttonP.grid(column=1, row=5)

        buttonR = Button(width=21, height=5, text="=",
                         command=self.entry1_get)
        buttonR.grid(column=2, row=5, columnspan=3)

        root.mainloop()

    def delete(self):
        self.main_entry.delete(0, END)

    def entry1_get(self):
        entry1 = self.main_entry.get()
        return print(entry1)

    def lenght_of_entry(self):
        entry1 = self.main_entry.get()
        length = len(entry1)
        return length

    def multi(self):
     # ____________________________________________________ jak to kurka zrobic mnozenie nie czaje XD help here
        self.firstarg = self.entry1_get()
        self.delete()
        self.sec = self.entry1_get()
        self.delete()
        multi = self.firstarg*self.sec

        return multi
    #____________________________________________________ jak to kurka zrobic mnozenie nie czaje XD help here
    def entry2_get(self):
        entry2 = self.main_entry.get()
        return print(entry2)