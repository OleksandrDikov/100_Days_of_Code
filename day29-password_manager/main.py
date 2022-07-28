from tkinter import messagebox
from tkinter import *
import random
import pyperclip
import json


def gen_pass():
    pass_length = 20
    symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!',
               '#', '$', '%', '&', '(', ')', '*', '+']

    password = ''.join(random.choice(symbols) for _ in range(pass_length))
    pass_entry.insert(0, password)
    pyperclip.copy(password)


def search_pass():
    site = web_entry.get()
    if not site:
        messagebox.showwarning(title="Warning", message="Please type site name")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showwarning(title="Warning", message="You don't have any data")
        else:
            if site in data:
                messagebox.showinfo(title=site, message=f"Login: {data[site]['username']}\n"
                                                        f"Password: {data[site]['password']}")
            else:
                messagebox.showinfo(title=site, message=f"You don't have account on this site")


    window.focus()
    web_entry.focus()


def save():
    new_data = {
        web_entry.get(): {
            "username": user_entry.get(),
            "password": pass_entry.get()
        }
    }
    if pass_entry.get() == "":
        messagebox.showwarning(title="Warning!", message="Password is required")
        pass_entry.focus()
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=2)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=2)
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

web_entry = Entry(width=22)
web_entry.grid(row=1, column=1)
web_entry.focus()
user_entry = Entry(width=37)
user_entry.grid(row=2, column=1, columnspan=2)
pass_entry = Entry(width=22)
pass_entry.grid(row=3, column=1)

src_button = Button(text="Search", width=11, command=search_pass)
src_button.grid(row=1, column=2)
gen_button = Button(text="Generate Password", width=11, command=gen_pass)
gen_button.grid(row=3, column=2)
add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
