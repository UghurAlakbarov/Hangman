import tkinter as tk
from tkinter.messagebox import showinfo

from Keyboard import Keyboard
from Trees import Trees
from Word import Word


class Game(tk.Tk):

    attempts_used = 0

    def __init__(self):

        super().__init__()
        
        self.initUI()
    
    def initUI(self):

        self.title("My Hangman Game")

        # keyboard
        self.keyboard = Keyboard(self)
        self.keyboard.pack(side="bottom")

        # hangman Tree
        self.tree = Trees(self)

        # guessed word so far
        self.word = Word(self)
    
    def letter_input(self, char):
        if char in self.word.word_being_guessed:
            self.word.add_letters_to_the_word(char)
            self.word.place_word()
        else:
            self.attempts_used += 1
            self.tree.change_picture()
        self.keyboard.letters[char]["state"] = "disabled"

        if "_" not in self.word.guessed_word_so_far:
                showinfo(title='Congratulations!', message='You won!')
                self.quit()

        if self.attempts_used == 6:
            showinfo(title='Oh no', message=f'You lost :(\nThe word was {self.word.word_being_guessed}')
            self.quit()

if __name__ == "__main__":
    hang = Game()
    hang.mainloop()
