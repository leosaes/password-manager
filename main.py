from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from pyperclip import copy
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  password_list = []

  [password_list.append(choice(letters)) for _ in range(randint(8, 10))]
  [password_list.append(choice(symbols)) for _ in range(randint(2, 4))]
  [password_list.append(choice(numbers)) for _ in range(randint(2, 4))]

  shuffle(password_list)

  password = "".join(password_list)

  password_input.insert(END,password)
  copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
  web = website_input.get()
  user = username_input.get()
  passw = password_input.get()
  data = {
    web: {
      "email": user,
      "password": passw
    }
  }

  if web == "" or user == "" or passw == "":
    messagebox.showinfo(title="Empty",message=f"Oops! You can't leave any fields empty!")
  else:  
      try:    
        with open("password-manager/data.json","r") as f:
          load = json.load(f)
          load.update(data)
      except FileNotFoundError:
        with open("password-manager/data.json","w") as f:
          json.dump(data,f,indent=4)
      else:
        with open("password-manager/data.json","w") as f:
          json.dump(load,f,indent=4)

      website_input.delete(0,END)
      password_input.delete(0,END)
# ---------------------------- PASSWORD SEARCH ------------------------------- #
def search():
  web = website_input.get()

  try:
    with open("password-manager/data.json","r") as f:
        load = json.load(f)
  except FileNotFoundError:
    messagebox.showinfo(title="Error",message="Not found")
  else:
    if web not in load:
      messagebox.showinfo(title="Oops",message="No details for the website")
    else:
      messagebox.showinfo(title=web,message=f"Email/User: {load[web]['email']}"
                        f"\nPassword: {load[web]['password']}")
# ---------------------------- UI SETUP ------------------------------- #
w = Tk()
w.title("Password Manager")
w.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
img = PhotoImage(file="password-manager/logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(column=1,row=0)

website = Label(text="Website:")
website.grid(column=0,row=1)

website_input = Entry(width=35)
website_input.focus()
website_input.grid(column=1,row=1,sticky="W")

username = Label(text="Email/Username:",padx=10)
username.grid(column=0,row=2)

username_input = Entry(width=55)
username_input.insert(END,"leosaes2002@gmail.com")
username_input.grid(column=1,row=2, columnspan=2,sticky="W")

password = Label(text="Password:")
password.grid(column=0,row=3)

password_input = Entry(width=35)
password_input.grid(column=1,row=3,sticky="W")

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2,row=3)

add_button = Button(text="Add",width=47,command=add)
add_button.grid(column=1,row=5, columnspan=2,sticky="S")

search_button = Button(text="Search",width=15,command=search)
search_button.grid(column=2,row=1)
w.mainloop()