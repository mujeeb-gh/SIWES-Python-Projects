from tkinter import *
from tkinter import messagebox
import random, pyperclip, json 

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

  symbols = ['!', '#', '$', '%', '&', '@', '(', ')', '*', '+']

  num_letters = random.randint(8, 10)
  num_numbers = random.randint(2, 4)
  num_symbols = random.randint(2, 4)

  password_letters = [random.choice(letters) for _ in range(num_letters)]
  password_numbers = [random.choice(numbers) for _ in range(num_numbers)]
  password_symbols = [random.choice(symbols) for _ in range(num_symbols)]

  password_list = password_letters + password_numbers + password_symbols
  random.shuffle(password_list)

  password = "".join(password_list)
  
  if len(password_entry.get()) > 0:
    password_entry.delete(0, END)
    
  password_entry.insert(0, password)
  pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
  """Adds specified entries to the data.txt file"""
  website = website_entry.get()
  email = email_entry.get()
  password = password_entry.get()
  json_data = {
    website: {
      "email": email,
      "password": password 
    }
  }
  if len(website) == 0 or len(password) == 0:
    messagebox.showinfo(title = "oops", message= "Please make sure you haven't left any fields empty")
  else:
    try:
      with open("C:/Users/Mike Nwabudike/Documents/Python_Learn/Udemy/100 Days of Code/Day_29 - password_manager/data.json", "r") as data_file:
        
        # Reading the old data
        loaded_data = json.load(data_file)
    except FileNotFoundError:
      with open("C:/Users/Mike Nwabudike/Documents/Python_Learn/Udemy/100 Days of Code/Day_29 - password_manager/data.json", "w") as data_file:
        json.dump(json_data, data_file, indent= 4)
    else:
      # Updating the old data with the new data
      loaded_data.update(json_data)
        
      with open("C:/Users/Mike Nwabudike/Documents/Python_Learn/Udemy/100 Days of Code/Day_29 - password_manager/data.json", "w") as data_file:
        # Saving the updated data
        json.dump(loaded_data, data_file, indent= 4)
    finally:
      website_entry.delete(0, END)
      password_entry.delete(0, END)
      
      
# -------------------- SEARCH PASSWORD AND EMAIL ----------------------- #
def find_password():
  website = website_entry.get()
  try:
    with open("C:/Users/Mike Nwabudike/Documents/Python_Learn/Udemy/100 Days of Code/Day_29 - password_manager/data.json", "r") as data_file:
      loaded_data = json.load(data_file)
  except FileNotFoundError:
    messagebox.showinfo(title = "Error", message= "No Data File Found")
  else:
    if website in loaded_data:
      email = loaded_data[website]["email"]
      password = loaded_data[website]["password"]
      messagebox.showinfo(title = website, message = f"Email: {email}\nPassword: {password}")
    else:
      messagebox.showinfo(title = "Error", message= f"No saved details for {website}")

# ---------------------------- UI SETUP ------------------------------- #
# Window setup
window = Tk()
window.title("Password Manager")
window.config(padx= 50, pady = 50, bg = YELLOW)
window.minsize(600, 400)

# Image Canvas
canvas = Canvas(width = 200, height = 200)
canvas.config(bg = YELLOW, highlightthickness= 0)
pass_img = PhotoImage(file = "C:/Users/Mike Nwabudike/Documents/Python_Learn/Udemy/100 Days of Code/Day_29 - password_manager/logo.png")
canvas.create_image(100, 100, image = pass_img)
canvas.grid(column= 1, row= 0)

# Labels
website_label = Label(text = "Website:")
website_label.config(bg = YELLOW)
website_label.grid(row= 1,column= 0)
email_label = Label(text = "Email/Username:")
email_label.config(bg = YELLOW)
email_label.grid(row= 2, column= 0)
password_label = Label(text = "Password:")
password_label.config(bg = YELLOW)
password_label.grid(row= 3, column= 0)


# Entries
website_entry = Entry(width= 35)
website_entry.grid(row = 1, column= 1)
website_entry.focus()
email_entry = Entry(width= 70)
email_entry.grid(row= 2, column= 1, columnspan= 2)
email_entry.insert(0, "lamilolade@gmail")
password_entry = Entry(width = 35)
password_entry.grid(row = 3, column= 1)

# Buttons
generate_password_button = Button(text = "Generate Password", width= 28, command= generate_password)
generate_password_button.grid(row = 3, column= 2)

add_button = Button(text = "Add", width= 59, command= save)
add_button.grid(row = 4, column = 1, columnspan= 2)

search_button = Button(text = "Search", width = 28, command = find_password)
search_button.grid(row= 1, column= 2)


window.mainloop()

# ---------------------------- DELETED CODE ------------------------------- #
'''is_ok = messagebox.askokcancel(title= f"{website}", message= f"Details entered:\nEmail: {email} \nPassword: {password} \n Is it ok to save?")
    
    if is_ok:'''