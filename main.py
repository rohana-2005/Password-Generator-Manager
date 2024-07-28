import json
from tkinter import *
import random
import pyperclip
from tkinter import messagebox

def password_generator():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    symbols = '!#$%&()*+'
    numbers = '0123456789'

    password_letters = [random.choice(letters) for n in range(random.randint(4, 6))]
    password_symbols = [random.choice(symbols) for n in range(random.randint(4, 6))]
    password_numbers = [random.choice(numbers) for n in range(random.randint(4, 6))]

    password_list = password_symbols+password_letters+password_numbers
    random.shuffle(password_list)
    pass_word = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, pass_word)
    pyperclip.copy(pass_word)


def save():
    get_website = website_input.get()
    get_email = email_input.get()
    get_password = password_input.get()

    new_data = {
        get_website: {
            "Email": get_email,
            "Password": get_password
        }
    }

    if len(get_website) == 0 or len(get_password) == 0 or len(get_email) == 0:
        messagebox.showerror(title="Oops!", message="Please dont leave any fields blank!")
    else:
        is_ok = messagebox.askokcancel(title=f"Confirmation", message=f"Details entered:\nWebsite: {get_website}\nEmail/Username: {get_email}\nPassword: {get_password}\nDo you want to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                data = {}
            except json.JSONDecodeError:
                data = {}
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
            website_input.delete(0, END)
            password_input.delete(0, END)


def find_password():
    get_website = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error!", message="No Data file found!")
    except json.JSONDecodeError:
        messagebox.showerror(title="Error!", message="File Corrupted!")
    else:
        if get_website in data:
            get_email = data[get_website]["Email"]
            get_password = data[get_website]["Password"]
            messagebox.showinfo(title=get_website, message=f"Email: {get_email}\nPassword: {get_password}")
        else:
            messagebox.showerror(title="Error!", message=f"No details for {get_website}")



window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website = Label(text="Website: ")
website.grid(column=0, row=1)

email = Label(text="Email/Username: ")
email.grid(column=0, row=2)

password = Label(text="Password: ")
password.grid(column=0, row=3)

website_input = Entry(width=30)
website_input.focus()
website_input.grid(column=1, row=1)

search = Button(text="Search", width=15, command=find_password)
search.grid(column=2, row=1)

email_input = Entry(width=50)
email_input.insert(0, "rohanamahimkar28@gmail.com")
email_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=30)
password_input.grid(column=1, row=3)

generate_password = Button(text="Generate Password", width=15, command=password_generator)
generate_password.grid(column=2, row=3)

add = Button(text="Add", width=45, command=save)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()
