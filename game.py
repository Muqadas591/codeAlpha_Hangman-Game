# Hangman Game with multiple words at different levels
import tkinter as tk
from tkinter import messagebox

# The list of levels with words to be guessed
levels = [
    {"name": "Easy", "words": ["cat", "dog", "sun"]},
    {"name": "Medium", "words": ["house", "car", "tree"]},
    {"name": "Hard", "words": ["python", "java", "ruby"]}
]

class HangmanGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Hangman Game")
        self.level = None
        self.word = None
        self.guessed = None
        self.lives = 10
        self.current_word = 0
        self.create_level_selection()

    def create_level_selection(self):
        self.level_selection_frame = tk.Frame(self.window)
        self.level_selection_frame.pack()
        tk.Label(self.level_selection_frame, text="Select a level:").pack()
        for i, level in enumerate(levels):
            tk.Button(self.level_selection_frame, text=level["name"], command=lambda i=i: self.select_level(i)).pack()

    def select_level(self, level_index):
        self.level = levels[level_index]
        self.level_selection_frame.destroy()
        self.create_game_frame()

    def create_game_frame(self):
        self.game_frame = tk.Frame(self.window)
        self.game_frame.pack()
        self.word = self.level["words"][self.current_word]
        self.guessed = ["_"] * len(self.word)
        self.word_label = tk.Label(self.game_frame, text=" ".join(self.guessed))
        self.word_label.pack()
        self.lives_label = tk.Label(self.game_frame, text=f"Lives: {self.lives}")
        self.lives_label.pack()
        self.level_label = tk.Label(self.game_frame, text=f"Level: {self.level['name']}")
        self.level_label.pack()
        self.word_number_label = tk.Label(self.game_frame, text=f"Word {self.current_word + 1} of {len(self.level['words'])}")
        self.word_number_label.pack()
        self.guess_entry = tk.Entry(self.game_frame)
        self.guess_entry.pack()
        tk.Button(self.game_frame, text="Guess", command=self.check_guess).pack()

    def check_guess(self):
        guess = self.guess_entry.get()
        self.guess_entry.delete(0, tk.END)
        if guess in self.word:
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.guessed[i] = guess
        else:
            self.lives -= 1
            messagebox.showinfo("Incorrect!", "You lost a life.")
        self.word_label['text'] = " ".join(self.guessed)
        self.lives_label['text'] = f"Lives: {self.lives}"
        if "_" not in self.guessed:
            messagebox.showinfo("Congratulations!", "You won the current word!")
            self.current_word += 1
            if self.current_word == len(self.level["words"]):
                messagebox.showinfo("Congratulations!", f"You completed the {self.level['name']} level!")
                self.window.quit()
            else:
                self.game_frame.destroy()
                self.create_game_frame()
        elif self.lives == 0:
            messagebox.showinfo("Game Over!", "You lost all lives.")
            self.window.quit()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = HangmanGame()
    game.run()

# The list of levels with words to be guessed
levels = [
    {"name": "Easy", "words": ["cat", "dog", "sun"]},
    {"name": "Medium", "words": ["house", "car", "tree"]},
    {"name": "Hard", "words": ["python", "java", "ruby"]}
]

# The number of lives the player has
lives = 10

# The current level of player and word index
current_level = 0
current_word = 0

# The main game loop
while lives > 0 and current_level < len(levels):
    # Get the current level and word
    level = levels[current_level]
    word = level["words"][current_word]

    # The guessed letters for the current word
    guessed = ["_"] * len(word)

    # The word loop
    while "_" in guessed and lives > 0:
        # Print the current state of the word
        print(" ".join(guessed))
        print(f"Lives: {lives}")
        print(f"Level: {level['name']}")
        print(f"Word {current_word + 1} of {len(level['words'])}")

        # Ask the player for a letter
        letter = input("Guess a letter: ")

        # Check if the letter is in the word
        if letter in word:
            # Reveal the correct letter in the correct position
            for i in range(len(word)):
                if word[i] == letter:
                    guessed[i] = letter
        else:
            # Decrease the number of lives
            lives -= 1
            print("Incorrect! ")

    # Check if the player has won the current word
    if "_" not in guessed:
        print("Congratulations! You won the current word!")
        current_word += 1

        # Check if the player has completed the current level
        if current_word == len(level["words"]):
            print(f"Congratulations! You completed the {level['name']} level!")
            current_level += 1
            current_word = 0
    else:
        print("Game over! You lost a life.")

# Check if the player has completed all levels
if current_level == len(levels):
    print("Congratulations! You completed all levels!")
else:
    print("Game over! You lost all lives.")
