from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from pyperclip import copy
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

  if web == "" or user == "" or passw == "":
    messagebox.showinfo(title="Empty",message=f"Oops! You can't leave any fields empty!")
  else:     
    is_ok = messagebox.askokcancel(title=web,message=f"These are the details entered:" 
                          f"\nEmail: {user} \nPassword: {passw} \nIs it ok to save?")

    if is_ok == True:
      with open("password-manager/data.txt","a") as f:
        f.write(f"\n{web} | {user} | {passw}")
      website_input.delete(0,END)
      password_input.delete(0,END)
  
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
website_input.grid(column=1,row=1, columnspan=2)

username = Label(text="Email/Username:")
username.grid(column=0,row=2)

username_input = Entry(width=35)
username_input.insert(END,"leosaes2002@gmail.com")
username_input.grid(column=1,row=2, columnspan=2)

password = Label(text="Password:")
password.grid(column=0,row=3)

password_input = Entry(width=35)
password_input.grid(column=1,row=3, columnspan=2)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2,row=3)

add_button = Button(text="Add",width=36,command=add)
add_button.grid(column=1,row=5, columnspan=2)

w.mainloop()