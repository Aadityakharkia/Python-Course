'''
from tkinter import *

window = Tk()
window.title("My first GUI Programme")
window.minsize(width=500,height=300)

# Label
def button_clicked():
    my_label.config(text="Botton got Clicked")

my_label = Label(text="I am a Label")
my_label.pack()


button = Button(text="Click Me", command=button_clicked)
button.pack()


window.mainloop()

# Unlimited Arguments

def add(*args):
    total = 0
    for n in args:
        total += n
    print(total)

add(5,6,7,8,9)
'''

from tkinter import *


window = Tk()
window.title("My first GUI Programme")
window.minsize(width=500, height=500)


label = Label(text="I am a Label")
label.config(text="New Text")
label.grid(column=0 ,row=0)

button = Button(text="Click Me")
button.grid(column=1,row=1)

button_2 = Button(text="Click Me")
button_2.grid(column=2,row=0)

entry = Entry(width=10)
print(entry.get())
entry.grid(column=3,row=2)


window.mainloop()

