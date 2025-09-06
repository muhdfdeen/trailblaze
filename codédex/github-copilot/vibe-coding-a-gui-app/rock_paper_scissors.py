"""
Create a Rock Paper Scissors game where the player inputs their choice
and plays against a computer that randomly selects its move,
with the game showing who won each round.
Add a score counter that tracks player and computer wins,
and allow the game to continue until the player types "quit".
"""
import random
import tkinter as tk
from tkinter import ttk, messagebox

def determine_winner(player, computer):
    """
    Determines the outcome of a Rock-Paper-Scissors game between the player and the computer.

    Args:
        player (str): The player's choice. Should be one of "Rock", "Paper", or "Scissors".
        computer (str): The computer's choice. Should be one of "Rock", "Paper", or "Scissors".

    Returns:
        str: The result of the game:
            - "win" if the player wins,
            - "lose" if the player loses,
            - "draw" if it's a tie.
    """
    allowed_choices = {"rock", "paper", "scissors"}
    player = player.strip().lower()
    computer = computer.strip().lower()
    if player not in allowed_choices or computer not in allowed_choices:
        raise ValueError("Invalid choice. Choices must be 'Rock', 'Paper', or 'Scissors'.")
    if player == computer:
        return "draw"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "win"
    else:
        return "lose"

class RockPaperScissorsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rock Paper Scissors")
        self.geometry("350x320")
        self.resizable(False, False)
        self.player_score = 0
        self.computer_score = 0
        self.tie_score = 0  # Track ties
        self.choices = ["Rock", "Paper", "Scissors"]
        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self, text="Choose Rock, Paper, or Scissors:")
        self.label.pack(pady=10)

        self.buttons_frame = ttk.Frame(self)
        self.buttons_frame.pack(pady=10)
        for choice in self.choices:
            button = ttk.Button(self.buttons_frame, text=choice, command=lambda c=choice: self.play_round(c))
            button.pack(side=tk.LEFT, padx=5)

        self.result_label = ttk.Label(self, text="")
        self.result_label.pack(pady=10)

        self.score_label = ttk.Label(self, text="Player: 0 | Computer: 0")
        self.score_label.pack(pady=10)

        self.scoreboard_label = ttk.Label(
            self,
            text="Scoreboard\nPlayer Wins: 0\nComputer Wins: 0\nTies: 0",
            font=("Arial", 10),
            relief=tk.GROOVE,
            padding=5
        )
        self.scoreboard_label.pack(pady=5)

        self.quit_button = ttk.Button(self, text="Quit", command=self.quit_game)
        self.quit_button.pack(pady=10)

    def play_round(self, player_choice):
        computer_choice = random.choice(self.choices)
        result = determine_winner(player_choice, computer_choice)
        if result == "win":
            self.player_score += 1
            result_text = f"You win! {player_choice} beats {computer_choice}."
        elif result == "lose":
            self.computer_score += 1
            result_text = f"You lose! {computer_choice} beats {player_choice}."
        else:
            self.tie_score += 1
            result_text = f"It's a draw! You both chose {player_choice}."
        self.result_label.config(text=result_text)
        self.score_label.config(text=f"Player: {self.player_score} | Computer: {self.computer_score}")
        self.scoreboard_label.config(
            text=f"Scoreboard\nPlayer Wins: {self.player_score}\nComputer Wins: {self.computer_score}\nTies: {self.tie_score}"
        )

    def quit_game(self):
        if messagebox.askokcancel("Quit", "Do you really want to quit?"):
            self.destroy()

if __name__ == "__main__":
    app = RockPaperScissorsApp()
    app.mainloop()