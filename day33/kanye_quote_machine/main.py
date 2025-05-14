from tkinter import *
import requests

#Command func
def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)

#Window
window = Tk()
window.title("Kanye Says...")
window.config(padx=50,pady=50)

#Canvas
canvas = Canvas(width=300,height=414)
background_image = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_image)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "bold"),fill="white")
canvas.grid(row=0,column=0)

#Button
kanye_photo = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_photo, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1,column=0)

window.mainloop()