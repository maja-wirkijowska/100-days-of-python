from tkinter import *

# window
window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)

# label
my_label = Label(text="This is a Label", font=("Arial", 24))
# my_label.pack(side="left")
my_label.pack()

my_label["text"] = "New Text"


# button - must be clicked right in the middle
def button_clicked():
    print("Button was clicked")
    new_text = entry.get()
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked)
button.pack()

# entry
entry = Entry(width=10)
entry.insert(END, string="Starter Text")
entry.pack()

# text
text = Text(height=5, width=30)
text.focus()  # curser
text.insert(END, "example text of multiline text box")
print(text.get("1.0", END))
text.pack()


# spinbox
def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# scale
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# check mark box
def checkmark_used():
    print(checked_state.get())


checked_state = IntVar()
checkmark = Checkbutton(text="Is on?", variable=checked_state, command=checkmark_used)
checked_state.get()
checkmark.pack()


# radio buttons
def radio_used():
    print(radio_state.get())


radio_state = IntVar()
radio_button1 = Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radio_button2 = Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
radio_button1.pack()
radio_button2.pack()


# list box
def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
letters = ["A", "B", "C", "D"]
for item in letters:
    listbox.insert(letters.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()
