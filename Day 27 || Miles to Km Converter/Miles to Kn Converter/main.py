from tkinter import *

#-----------------------------------------------Function -------------------
def calculate():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_output.config(text=f"{km}")

#-----------------------------------------------Creating UI -------------------

window = Tk()
window.title("Mile to Kilometer Convertor")
window.config(padx=20,pady=20)

text_1 = Label(text="Miles: - ")
text_1.grid(column=0,row=1)

miles_input = Entry(width=5)
miles_input.grid(column=1,row=1)

text_2 = Label(text="== Kilometer :- ")
text_2.grid(column=2,row=1)

kilometer_output = Label(width=5,text="0")
kilometer_output.grid(column=3,row=1)

button = Button(text="Convert",command=calculate)
button.grid(column=2,row=2)

window.mainloop()