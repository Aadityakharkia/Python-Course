# Creating password manager.

from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for item in range(nr_letters)]
    password_symbols = [random.choice(symbols) for item in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for item in range(nr_numbers)]

    password_list = password_symbols + password_numbers + password_letters

    random.shuffle(password_list)
    password_random = "".join(password_list)
    password_input.insert(0,password_random)
    pyperclip.copy(password_random)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website_1 = website_input.get().lower()
    email_1 = email_input.get()
    password_1 = password_input.get()
    new_data = {
        website_1:{
        "email" : email_1,
        "password" : password_1
        }
    }

    if len(website_1)==0 or len(password_1)==0 or len(email_1) == 0:
        messagebox.showinfo(title="Oops",message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json","w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_input.delete(0,END)
            password_input.delete(0, END)

def find_password():
    wesite_2 = website_input.get().lower()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if wesite_2 in data:
            email = data[wesite_2]["email"]
            password = data[wesite_2]["password"]
            messagebox.showinfo(title=wesite_2, message=f"Email:{email}\n Password:{password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {wesite_2} exists")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(pady=50,padx=50,)
window.title("Password Manager")

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0,column=1)

website = Label(text="Website:")
website.grid(row=1,column=0)
website_input = Entry(width=21)
website_input.grid(row=1,column=1)
website_input.focus()

website_search = Button(text="Search",width=12, command=find_password)
website_search.grid(row=1,column=2,columnspan=1)


email = Label(text="Email/Username:")
email.grid(row=2,column=0)
email_input = Entry(width=35)
email_input.grid(row=2,column=1,columnspan=2)
email_input.insert(0,"aadityakharkia10@gmail.com")

password = Label(text="Password")
password.grid(row=3,column=0)
password_input = Entry(width=21)
password_input.grid(row=3,column=1,columnspan=1)
generate_password = Button(text="Generate Password",command=generate_password)
generate_password.grid(row=3,column=2)

add_button = Button(text="Add",width=36,command=add_password)
add_button.grid(row=4,column=1,columnspan=2)



window.mainloop()