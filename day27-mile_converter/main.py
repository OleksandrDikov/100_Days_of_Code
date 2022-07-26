from tkinter import *
from tkinter.ttk import *


def convert():
    miles = float(input_entry.get())
    output_label.config(text=round(miles * 1.6, 2))


window = Tk()
window.title("Mile to KM Converter")
window.config(padx=20, pady=10)

Label(text="is equal to").grid(row=1, column=0)
Label(text="Miles").grid(row=0, column=2)
Label(text="Km").grid(row=1, column=2)

input_entry = Entry(width=9)
input_entry.grid(row=0, column=1)
output_label = Label(text="0")
output_label.grid(row=1, column=1)

Button(text="Calculate", command=convert).grid(row=2, column=1)
window.mainloop()
