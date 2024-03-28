import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

# Function to play the game
def play_game():
    user_choice = user_choice_var.get()
    computer_choice = random.choice(choices)

    result = determine_winner(user_choice, computer_choice)

    messagebox.showinfo("Result", f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n{result}")

# Create the main window
window = tk.Tk()
window.title("Rock-Paper-Scissors Game")

# Instructions label
instructions_label = tk.Label(window, text="Choose rock, paper, or scissors:")
instructions_label.pack()

# User choice radio buttons
user_choice_var = tk.StringVar()
choices = ["rock", "paper", "scissors"]
for choice in choices:
    tk.Radiobutton(window, text=choice, variable=user_choice_var, value=choice).pack()

# Button to play the game
play_button = tk.Button(window, text="Play", command=play_game)
play_button.pack()

# Run the main event loop
window.mainloop()
