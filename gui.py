from tkinter import *
import tkinter


class Gui:

    def __int__(self):
        self.last_input = None
        self.operation_button_pressed = False
        self.main_entry = None
        self.operation = None
        self.current_result = 0
        self.run_tkinter()
        self.value = 0

    def run_tkinter(self):

        root = tkinter.Tk()
        root.title("Calculator")
        root.config(padx=100, pady=20)

        self.main_entry = Entry(width=17, font=("Times", "30", "bold"))
        self.main_entry.grid(column=0, row=0, columnspan=4)

        self.przygotowanie_przyciskow_funkcyjnych()
        self.przygotowanie_przyciskow_liczbowych()

        root.mainloop()

    def przygotowanie_przyciskow_funkcyjnych(self):

        buttonC = Button(width=10, height=5, text="C", command=self.clear_screen)
        buttonC.grid(column=0, row=1)

        button_mnozenie = Button(width=10, height=5, text="X", command=lambda: self.set_operation("X"))
        button_mnozenie.grid(column=1, row=1)

        button_dzielenie = Button(width=10, height=5, text="/", command=lambda: self.set_operation("/"))
        button_dzielenie.grid(column=2, row=1)

        button_dodawanie = Button(width=10, height=11, text="+", command=lambda: self.set_operation("+"))
        button_dodawanie.grid(column=3, row=1, rowspan=2)

        button_odejmowanie = Button(width=10, height=5, text="-", command=lambda: self.set_operation("-"))
        button_odejmowanie.grid(column=3, row=3)

        button_procent = Button(width=10, height=5, text="%", command=lambda: self.procent_pressed(1))
        button_procent.grid(column=3, row=4)

        buttonR = Button(width=21, height=5, text="=", cursor="dot", command=self.result)
        buttonR.grid(column=2, row=5, columnspan=3)

    def przygotowanie_przyciskow_liczbowych(self):
        self.bg_color = "Grey"
        button1 = Button(width=10, height=5, bg=self.bg_color, text="1", command=lambda: self.insert_to_entry(1))
        button1.grid(column=0, row=2)

        button2 = Button(width=10, height=5, bg=self.bg_color, text="2", command=lambda: self.insert_to_entry(2))
        button2.grid(column=1, row=2)

        button3 = Button(width=10, height=5, bg=self.bg_color, text="3", command=lambda: self.insert_to_entry(3))
        button3.grid(column=2, row=2)

        button4 = Button(width=10, height=5, bg=self.bg_color, text="4", command=lambda: self.insert_to_entry(4))
        button4.grid(column=0, row=3)

        button5 = Button(width=10, height=5, bg=self.bg_color, text="5", command=lambda: self.insert_to_entry(5))
        button5.grid(column=1, row=3)

        button6 = Button(width=10, height=5, bg=self.bg_color, text="6", command=lambda: self.insert_to_entry(6))
        button6.grid(column=2, row=3)

        button7 = Button(width=10, height=5, bg=self.bg_color, text="7", command=lambda: self.insert_to_entry(7))
        button7.grid(column=0, row=4)

        button8 = Button(width=10, height=5, bg=self.bg_color, text="8", command=lambda: self.insert_to_entry(8))
        button8.grid(column=1, row=4)

        button9 = Button(width=10, height=5, bg=self.bg_color, text="9", command=lambda: self.insert_to_entry(9))
        button9.grid(column=2, row=4)

        button0 = Button(width=10, height=5, bg=self.bg_color, text="0", command=lambda: self.insert_zero())
        button0.grid(column=0, row=5)

        buttonP = Button(width=10, height=5, bg=self.bg_color, text=".", command=lambda: self.insert_dot())
        buttonP.grid(column=1, row=5)

    def clear_screen(self):
        self.main_entry.delete(0, END)

    def take_value_from_screen(self):
        return self.main_entry.get()

    def len_oF_value(self):
        return len(self.main_entry.get())

    def insert_to_entry(self, value):
        if self.operation_button_pressed:
            self.clear_screen()
            self.operation_button_pressed = False
        self.main_entry.insert(self.len_oF_value(), value)

    def insert_dot(self):
        if "." not in self.take_value_from_screen():
            self.insert_to_entry(".")

    def insert_zero(self):
        if len(self.main_entry.get()) == 0:
            pass
        else :
            self.insert_to_entry(0)

    def procent_pressed(self, val):
        self.value = 0 + val

    def set_operation(self, operation):
        self.last_input = self.take_value_from_screen()
        self.operation = operation
        self.operation_button_pressed = True


    def result(self):
        self.is_procent_pressed = False
        current_input = self.take_value_from_screen()
        if self.operation == "X":
            if self.value !=0:
                self.current_result = (float(self.last_input) * (float(self.last_input)*float(current_input))/100)
                self.value = 0
            else:
                self.current_result = float(self.last_input) * float(current_input)
                self.value = 0
        if self.operation == "/":
            if float(current_input) == float(0):
                self.current_result= "Nie dziel przez zero"
            elif self.value != 0:
                self.current_result = (
                            float(self.last_input) / ((float(self.last_input) * float(current_input)) / 100))
                self.value = 0
            else:
                self.current_result = float(self.last_input) / float(current_input)
                self.value = 0

        if self.operation == "+":
            if self.value !=0:
                self.current_result = (float(self.last_input) + (float(self.last_input)*float(current_input))/100)
                self.value = 0
            else:
                self.current_result = float(self.last_input) + float(current_input)
                self.value = 0
        if self.operation == "-":
            if self.value !=0:
                self.current_result = (float(self.last_input) - (float(self.last_input)*float(current_input))/100)
                self.value = 0
            else:
                self.current_result = float(self.last_input) - float(current_input)
                self.value = 0
        self.clear_screen()
        self.insert_to_entry(self.current_result)
