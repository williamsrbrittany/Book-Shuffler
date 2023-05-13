# A book recommendation app that randomly recommends a book
from tkinter import *
import random

# basic variables for colors and fonts
FONT_NAME = "Courier"
PURPLE = "#957DAD"
PINK = "#E0BBE4"
BEIGE = "#FFDFD3"

# the main window of application
window = Tk()
window.geometry("500x600")
window.title("Book Shuffler")
window.configure(bg=BEIGE)

canvas = Canvas(width=300, height=300, borderwidth=0, highlightthickness=0)
top_img = PhotoImage(file="BookShufflerlogo.png")
canvas.create_image(150, 150, image=top_img)
canvas.pack()
canvas.create_text(150, 300, text="Do you want a random romance book recommendation?", fill=PURPLE, font=("FONT_NAME", 15, "normal"))

rec_button = Button(window, text="Give it to me!", bg=PURPLE, font=FONT_NAME)
rec_button.config(fg='white', activebackground='BEIGE')
rec_button.pack()

# starts the application
window.mainloop()
