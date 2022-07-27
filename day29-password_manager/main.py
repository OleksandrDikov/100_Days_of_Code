from tkinter import messagebox
from tkinter import *
import random
import pyperclip


def gen_pass():
    pass_length = 20
    symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!',
               '#', '$', '%', '&', '(', ')', '*', '+']

    password = ''.join(random.choice(symbols) for _ in range(pass_length))
    pass_entry.insert(0, password)
    pyperclip.copy(password)


def save():
    if pass_entry.get() == "":
        messagebox.showwarning(title="Warning!", message="Password is required")
        pass_entry.focus()
    else:
        new_item = messagebox.askyesno(title="New item",
                                       message=f"Save password\n site: {web_entry.get()}\n login: {user_entry.get()}")
        if new_item:
            with open("data.txt", "a") as f:
                f.write(f"{web_entry.get()} | {user_entry.get()} | {pass_entry.get()}\n")
            web_entry.delete(0, 'end')
            pass_entry.delete(0, 'end')


window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file='logo.png')
canvas.create_image(130, 100, image=img)
canvas.grid(row=0, column=1)

web_label = Label(text="Website:")
web_label.grid(row=1, column=0)
user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0)
pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

web_entry = Entry(width=37)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()
user_entry = Entry(width=37)
user_entry.grid(row=2, column=1, columnspan=2)
pass_entry = Entry(width=22)
pass_entry.grid(row=3, column=1)

gen_button = Button(text="Generate Password", width=11, command=gen_pass)
gen_button.grid(row=3, column=2)
add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
