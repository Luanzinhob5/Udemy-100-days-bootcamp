from tkinter import *
import pandas as pd
import random

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
# ---------------------------- WORDs ------------------------------- #
try:
    data = pd.read_csv("/Users/berga/Documents/Programação atual/CursoUdemy/day31/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("/Users/berga/Documents/Programação atual/CursoUdemy/day31/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title ,text=f"French", fill="black")
    canvas.itemconfig(word ,text=f"{current_card["French"]}", fill="black")
    canvas.itemconfig(flash_card,image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)
    # random_word = random.choice(data.French)
    # front_card.itemconfig(title ,text=f"French")
    # front_card.itemconfig(word ,text=f"{random_word}")

def flip_card():
    canvas.itemconfig(title ,text=f"English",fill="white")
    canvas.itemconfig(word ,text=f"{current_card["English"]}", fill="white")
    canvas.itemconfig(flash_card,image=card_back_img)


def check_button():
    if current_card != {}:
        to_learn.remove(current_card)
        df = pd.DataFrame(to_learn)
        df.to_csv("/Users/berga/Documents/Programação atual/CursoUdemy/day31/data/words_to_learn.csv",index=False)
    next_card()
# ---------------------------- UI SETUP ------------------------------- #
#Window
window = Tk()
window.title("flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)
#Front card
canvas = Canvas(width=800, height=526, bg = BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="/Users/berga/Documents/Programação atual/CursoUdemy/day31/images/card_front.png")
flash_card = canvas.create_image(400, 263, image=card_front_img)
word = canvas.create_text(400, 263, text="Word", fill="black", font=( "Ariel",35, "bold"))
title = canvas.create_text(400, 150, text="Title", fill="black", font=( "Ariel",28, "italic"))
canvas.grid(row=0,column=0,columnspan=2)

#Back card
card_back_img = PhotoImage(file="/Users/berga/Documents/Programação atual/CursoUdemy/day31/images/card_back.png")

#Right
right_img = PhotoImage(file="/Users/berga/Documents/Programação atual/CursoUdemy/day31/images/right.png")
right = Button(image=right_img ,bg=BACKGROUND_COLOR,command=check_button)
right.grid(row=1,column=1)


#Wrong
wrong_img = PhotoImage(file="/Users/berga/Documents/Programação atual/CursoUdemy/day31/images/wrong.png")
wrong = Button(image=wrong_img,bg=BACKGROUND_COLOR,command=next_card)
wrong.grid(row=1,column=0)


window.mainloop()