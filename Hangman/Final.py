# Hangman Game

# For GUI
import tkinter as tk

# Words for hangman
from wordlist import words

# To select random words
import random

#Set the Window
window = tk.Tk()
window.title("Hangman Game")
window.config(relief="groove", padx=5, pady=5)
window.geometry("800x800")

# Labels and input

# For extra space at the top of the window.
empty_label = tk.Label(text=" ")
empty_label.pack(pady=30)

# Instructions for the player.
hello_label = tk.Label(window, text= "Guess a letter to find the word", font = ("Helvetica",20))
hello_label.pack(pady=10)

control_frame = tk.Frame(window)
control_frame.pack(pady=10)

label = tk.Label(window, text=" ", font = ("Helvetica",20))
label.pack(pady=10)

lives_label = tk.Label(window, text="Lives remaining : 6", font = ("Helvetica",20))
lives_label.pack(pady=10)

result_label = tk.Label(window, text="", font = ("Helvetica",20))
result_label.pack()

play_again_button = tk.Button(control_frame, font=("helvetica", 15), bg="light grey", text="Play Again", command=lambda: game.reset_game())
quit_button = tk.Button(control_frame, font=("Helvetica", 15), bg="light grey", text="Quit", command=window.quit)

# Canvas for Hangman
canvas = tk.Canvas(window, width = 300, height = 300)
canvas.pack(pady=20)

# Draw Hangman
def show_buttons():
    play_again_button.pack(pady=10)
    quit_button.pack(pady=10)

def hide_buttons():
    quit_button.pack_forget()
    play_again_button.pack_forget()

def quit_game():
    window.quit()

class HangmanGame:
    def __init__(self):
        self.words = words
        self.lives = 8
        self.random_word = random.choice(self.words)
        self.guessed_word = ["_"] * len(self.random_word)

        self.entry = tk.Entry(control_frame, width=10, font=("Helvetica", 20), justify="center")
        self.button = tk.Button(control_frame, font=("helvetica", 15), bg="light grey", text="Guess", command=lambda: game.guess())

        self.reset_game()

    def reset_game(self):
        self.lives = 8
        self.random_word = random.choice(self.words)
        self.guessed_word = ["_"] * len(self.random_word)
        self.update_display()
        hide_buttons()
        result_label.config(text="")
        canvas.delete("all")

        self.show_widgets()

    def show_widgets(self):
        self.entry.pack(pady=10)
        self.button.pack(pady=10)

    def hide_widgets(self):
        self.entry.pack_forget()
        self.button.pack_forget()

    def draw_hangman(self):
        if self.lives == 7:
            canvas.create_line(100,50,200,50, width=5)
        elif self.lives == 6:
            canvas.create_line(150,50,150,100, width=5)
        elif self.lives == 5:
            canvas.create_oval(140, 100, 160, 120, width=5)
        elif self.lives == 4:
            canvas.create_line(150, 120, 150, 170, width=5)
        elif self.lives == 3:
            canvas.create_line(150, 120, 180, 150, width=5)
        elif self.lives == 2:
            canvas.create_line(150, 120, 120, 150, width=5)
        elif self.lives == 1:
            canvas.create_line(150, 170, 180, 200, width=5)
        elif self.lives == 0:
            canvas.create_line(150, 170, 120, 200, width=5)

    def check_guess(self, guess):
        if len(guess) != 1 or not guess.isalpha():
            result_label.config(text="Error, Please enter a single letter")
            return
        if guess in self.random_word:
            for i in range(len(self.random_word)):
                if self.random_word[i] == guess:
                    self.guessed_word[i] = guess
        else:
            self.lives -= 1

        self.update_display()
        self.game_over()

    def guess(self):
        guess = self.entry.get().lower()
        if guess:
            self.check_guess(guess)
        self.entry.delete(0, tk.END)

    def update_display(self):
        lives_label.config(text=f"Lives remaining: {self.lives}")
        label.config(text=" ".join(self.guessed_word))
        self.draw_hangman()

    def game_over(self):
        if "_" not in self.guessed_word:
            result_label.config(text="You Won! Congratulations")
            show_buttons()
            self.hide_widgets()
        elif self.lives == 0:
            result_label.config(text=f"Game Over! The word was: {self.random_word}")
            show_buttons()
            self.hide_widgets()

game = HangmanGame()

window.mainloop()