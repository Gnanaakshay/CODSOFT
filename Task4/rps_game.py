from tkinter import *
import random

# Main window
root = Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x450")
root.config(bg="lightblue")

# Scores
user_score = 0
computer_score = 0

# Function to play game
def play(user_choice):
    global user_score
    global computer_score

    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    user_label.config(text="You Chose : " + user_choice)
    computer_label.config(text="Computer Chose : " + computer_choice)

    # Game logic
    if user_choice == computer_choice:
        result = "It's a Tie!"

    elif user_choice == "Rock":
        if computer_choice == "Scissors":
            result = "You Win!"
            user_score = user_score + 1
        else:
            result = "Computer Wins!"
            computer_score = computer_score + 1

    elif user_choice == "Paper":
        if computer_choice == "Rock":
            result = "You Win!"
            user_score = user_score + 1
        else:
            result = "Computer Wins!"
            computer_score = computer_score + 1

    elif user_choice == "Scissors":
        if computer_choice == "Paper":
            result = "You Win!"
            user_score = user_score + 1
        else:
            result = "Computer Wins!"
            computer_score = computer_score + 1

    result_label.config(text=result)

    score_label.config(
        text="Your Score : " + str(user_score) +
             "    Computer Score : " + str(computer_score)
    )

# Reset function
def reset_game():
    global user_score
    global computer_score

    user_score = 0
    computer_score = 0

    user_label.config(text="You Chose : ")
    computer_label.config(text="Computer Chose : ")
    result_label.config(text="")
    score_label.config(text="Your Score : 0    Computer Score : 0")

# Heading
heading = Label(
    root,
    text="Rock Paper Scissors",
    font=("Arial", 20, "bold"),
    bg="lightblue",
    fg="darkblue"
)
heading.pack(pady=20)

# Instructions
instruction = Label(
    root,
    text="Choose Rock, Paper, or Scissors",
    font=("Arial", 12),
    bg="lightblue"
)
instruction.pack()

# Buttons
rock_button = Button(
    root,
    text="Rock",
    width=15,
    height=2,
    bg="white",
    command=lambda: play("Rock")
)
rock_button.pack(pady=10)

paper_button = Button(
    root,
    text="Paper",
    width=15,
    height=2,
    bg="white",
    command=lambda: play("Paper")
)
paper_button.pack(pady=10)

scissors_button = Button(
    root,
    text="Scissors",
    width=15,
    height=2,
    bg="white",
    command=lambda: play("Scissors")
)
scissors_button.pack(pady=10)

# Labels for choices
user_label = Label(
    root,
    text="You Chose : ",
    font=("Arial", 12),
    bg="lightblue"
)
user_label.pack(pady=5)

computer_label = Label(
    root,
    text="Computer Chose : ",
    font=("Arial", 12),
    bg="lightblue"
)
computer_label.pack(pady=5)

# Result label
result_label = Label(
    root,
    text="",
    font=("Arial", 15, "bold"),
    bg="lightblue",
    fg="red"
)
result_label.pack(pady=15)

# Score label
score_label = Label(
    root,
    text="Your Score : 0    Computer Score : 0",
    font=("Arial", 12, "bold"),
    bg="lightblue"
)
score_label.pack(pady=10)

# Reset button
reset_button = Button(
    root,
    text="Reset Game",
    width=15,
    height=2,
    bg="yellow",
    command=reset_game
)
reset_button.pack(pady=10)

# Exit button
exit_button = Button(
    root,
    text="Exit",
    width=15,
    height=2,
    bg="orange",
    command=root.destroy
)
exit_button.pack(pady=10)

# Run window
root.mainloop()

