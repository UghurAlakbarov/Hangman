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
        self.keyboard.grid(row=5, rowspan=3, column=0, columnspan=10)

        # hangman Tree
        self.tree = Trees(self)
        self.tree.grid(row=0, rowspan=5, column=5, columnspan=5)

        # guessed word so far
        self.word = Word(self)
        self.word.grid(row=2, rowspan=1, column=1, columnspan=3)
    
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
        
        self.keyboard.focus_set()

if __name__ == "__main__":
    hang = Game()
    hang.mainloop()
