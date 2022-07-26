import tkinter

window = tkinter.Tk()
window.title("My Program")
window.minsize(width=500, height=300)
window.configure(bg="purple", padx=50, pady=50)

def button_clicked():
    print("Button got clicked!")
    label.configure(text=entry.get())

label = tkinter.Label(text="First Label", font=("Arial", 24, "bold"))
label.grid(row=0, column=0)

button1 = tkinter.Button(text="First btn!", fg="red", command=button_clicked)
button1.grid(row=1, column=1)

button2 = tkinter.Button(text="Second btn!", command=button_clicked)
button2.grid(row=0, column=2)

entry = tkinter.Entry(fg="red", bg="white")
entry.grid(row=3, column=3)


window.mainloop()
