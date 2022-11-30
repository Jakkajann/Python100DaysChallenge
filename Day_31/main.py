from cgitb import text
from email.mime import image
from textwrap import fill
from tkinter import *
from numpy import flip
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
IMAGES_PATH = "Day_31/images/"
current_card = {}
to_learn = {}


try:
    data = pd.read_csv("Day_31/data/fwords_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("Day_31/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_know():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("Day_31/data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_img = PhotoImage(file=IMAGES_PATH + "card_front.png")
card_back_img = PhotoImage(file=IMAGES_PATH + "card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

unknown_image = PhotoImage(file=IMAGES_PATH + "wrong.png")
unknown_button = Button(image=unknown_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

check_image = PhotoImage(file=IMAGES_PATH + "right.png")
check_button = Button(image=check_image, highlightthickness=0, command=is_know)
check_button.grid(column=1, row=1)

next_card()

window.mainloop()