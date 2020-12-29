from tkinter import *



#---------------------------------- PASSWORD GENERATOR -------------------------- #

#---------------------------------- SAVE PASSWORD TO FILE -------------------------- #
def save_credentials_to_file():
    with open("data.txt",mode="a") as data_file:
        data_file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")

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
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3,column=2)
add_button = Button(text="Add",width=36,command=save_credentials_to_file)
add_button.grid(row=4,column=1,columnspan=2)





window.mainloop()