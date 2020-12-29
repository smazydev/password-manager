from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import json


#---------------------------------- PASSWORD GENERATOR -------------------------- #

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_entry.insert(0,password)


#---------------------------------- SAVE PASSWORD TO FILE -------------------------- #
def save_credentials_to_file():
    website_entry_data = website_entry.get()
    email_entry_data = email_entry.get()
    password_entry_data = password_entry.get()

    credentials_dict = {
        website_entry_data: {
            "email": email_entry_data,
            "password": password_entry_data,
        }
    }

    if len(website_entry_data) == 0 or len(password_entry_data) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json",mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json",mode="w") as data_file:
                json.dump(credentials_dict,data_file,indent=4)
        else:
            data.update(credentials_dict)
            with open("data.json",mode="w") as data_file:
                json.dump(data,data_file,indent=4)
        finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)

#---------------------------------- UI SETUP -------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(height=200,width=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(row=0,column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0,padx=10,pady=10)
password_label = Label(text="Password:")
password_label.grid(row=3,column=0,padx=10,pady=10)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"ali@email.com")
password_entry = Entry(width=17)
password_entry.grid(row=3,column=1)

#Buttons
generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3,column=2)
add_button = Button(text="Add",width=36,command=save_credentials_to_file)
add_button.grid(row=4,column=1,columnspan=2)






window.mainloop()