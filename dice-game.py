import tkinter as tk
import random


def roll_dice():
    return random.randint(1, 6)


def play_game():
    p1_roll = roll_dice()
    p2_roll = roll_dice()
    
    player1_result.config(text=f"Player 1 rolled: 🎲 {p1_roll}")
    player2_result.config(text=f"Player 2 rolled: 🎲 {p2_roll}")
    
    if p1_roll > p2_roll:
        result_label.config(text="🏆 Player 1 Wins!", fg="green")
    elif p2_roll > p1_roll:
        result_label.config(text="🏆 Player 2 Wins!", fg="blue")
    else:
        result_label.config(text="🤝 It's a Tie!", fg="orange")

root = tk.Tk()
root.title("🎲 Dice Game")
root.geometry("350x300")
root.configure(bg="black")

title_label = tk.Label(root, text="🎲 Dice Game", font=("Arial", 20, "bold"), fg="white", bg="black")
title_label.pack(pady=20)

player1_result = tk.Label(root, text="Player 1 rolled: ", font=("Arial", 14), fg="white", bg="black")
player1_result.pack()

player2_result = tk.Label(root, text="Player 2 rolled: ", font=("Arial", 14), fg="white", bg="black")
player2_result.pack()

result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), fg="yellow", bg="black")
result_label.pack(pady=10)

roll_button = tk.Button(root, text="Roll Dice 🎲", font=("Arial", 14), command=play_game, bg="#444", fg="white", padx=10, pady=5)
roll_button.pack(pady=20)

root.mainloop()
