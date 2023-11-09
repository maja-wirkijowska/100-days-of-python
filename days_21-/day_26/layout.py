from tkinter import *


def button_clicked():
    print("Button was clicked")
    new_text = entry.get()
    my_label.config(text=new_text)


# window
window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)

# label
my_label = Label(text="This is a Label", font=("Arial", 24))
my_label["text"] = "New Text"
my_label.grid(column=0, row=0)

# button
button = Button(text="Click Here", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="New Button", command=button_clicked)
button2.grid(column=2, row=0)

# entry
entry = Entry(width=10)
entry.insert(END, string="Starter Text")
entry.grid(column=3, row=2)

window.mainloop()
