import tkinter

window = tkinter.Tk()
window.title("My Program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="First Label", font=("Arial", 24, "bold"))
my_label.pack(side="top")


window.mainloop()
