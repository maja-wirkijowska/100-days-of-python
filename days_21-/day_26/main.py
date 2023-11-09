from tkinter import *


def calculate_unit_conversion(**kwargs):
    miles = float(entry.get())
    kms = miles * 1.6
    label_output.config(text=kms)


# window
window = Tk()
window.title("Miles to Kilometers")
window.minsize(width=200, height=100)

entry = Entry(width=10)
entry.insert(END, string="miles")
entry.grid(column=1, row=0)

label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=1)

label_output = Label(text="0")
label_output.grid(column=1, row=1)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate_unit_conversion)
button.grid(column=1, row=2)


window.mainloop()
