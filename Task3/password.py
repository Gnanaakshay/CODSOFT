# Simple Password Generator with UI using Tkinter

import random
import string
from tkinter import *

# Function to generate password
def generate_password():
    length = entry_length.get()

    if length.isdigit():
        length = int(length)

        # Characters used in password
        characters = string.ascii_letters + string.digits + string.punctuation

        password = ""

        # Generate password
        for i in range(length):
            password += random.choice(characters)

        # Show password
        result_label.config(text=password)

    else:
        result_label.config(text="Enter valid number")


# Main window
window = Tk()
window.title("Password Generator")
window.geometry("400x300")
window.config(bg="lightblue")

# Title
title_label = Label(
    window,
    text="Password Generator",
    font=("Arial", 18, "bold"),
    bg="lightblue"
)
title_label.pack(pady=20)

# Enter length
length_label = Label(
    window,
    text="Enter Password Length",
    font=("Arial", 12),
    bg="lightblue"
)
length_label.pack()

entry_length = Entry(window, font=("Arial", 12))
entry_length.pack(pady=10)

# Button
generate_button = Button(
    window,
    text="Generate Password",
    font=("Arial", 12),
    command=generate_password,
    bg="green",
    fg="white"
)
generate_button.pack(pady=10)

# Result
result_label = Label(
    window,
    text="Your Password Will Appear Here",
    font=("Arial", 12),
    bg="lightblue",
    wraplength=300
)
result_label.pack(pady=20)

# Run window
window.mainloop()