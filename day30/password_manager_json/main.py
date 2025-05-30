from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for  _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    input_password.delete(0,END)
    input_password.insert(0, f"{password}")

    pyperclip.copy(password)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = input_website.get()

    try:
        with open("data.json", "r") as data_file:
                data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")

    else:
        if website in data:
            messagebox.showinfo(title=website,message=f"Email: {data[website]["email"]}\nPassword: {data[website]["password"]}")
        else:
            messagebox.showinfo(title="Error", message="No details for the website exists")

    
    


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    password = input_password.get()
    email = input_email_user.get()
    website = input_website.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(password) == 0 or len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                #Reading the old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        
        else:
            #Updating the old data with new data
            data.update(new_data)

            with open("data.json","w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            input_website.delete(0,END)
            input_password.delete(0,END)
        # except:
        #     with open("data.json","w") as data_file:
        #         #Saving updated data
        #         json.dump(new_data, data_file, indent=4)

        #         input_website.delete(0,END)
        #         input_password.delete(0,END)
    
# ---------------------------- UI SETUP ------------------------------- #
#Window
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)


#Image 
canvas = Canvas(width=200, height=200)
mypass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=mypass_image)
canvas.grid(column=1,row=0)


#Website Label
label_website = Label(text="Website:")
label_website.grid(column=0,row=1)
#Email/Username label
label_email_user = Label(text="Email/Username:")
label_email_user.grid(column=0,row=2)
#Password label
label_password = Label(text="Password:")
label_password.grid(column=0,row=3)


#Website input
input_website = Entry(width=40)
input_website.grid(column=1,row=1,columnspan=2)
input_website.focus()
#Email/Username Input
input_email_user = Entry(width=40)
input_email_user.grid(column=1,row=2,columnspan=2)
input_email_user.focus()
input_email_user.insert(0, "bergaminilucas7@gmail.com")
#Password Input
input_password = Entry(width=22)
input_password.grid(column=1,row=3)
input_password.focus()


#Generate password Button
button_password = Button(text="Generate Password",command=password_generator)
button_password.grid(column=2,row=3)
#Add Button
button_add = Button(text="Add",width=34,command=save_password)
button_add.grid(column=1,row=4,columnspan=2)
#Search Button
button_search = Button(text="Search",command= find_password)
button_search.grid(column=2, row=1)





window.mainloop()