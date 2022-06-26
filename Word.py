import random
from tkinter import ttk


class Word(ttk.Frame):

    """
    1) Generates the word
    2) Shows how much of the word has been guessed so far
    """
    
    guessed_word_so_far_label = None

    def __init__(self, master):
        super().__init__(master)

        self.master = master

        self.create_word()
        self.place_word()
    
    def create_word(self):
        with open('assets/words.txt') as open_file:
            self.word_being_guessed = random.choice(open_file.read().splitlines())
        # print(self.word_being_guessed)

        self.guessed_word_so_far = ["_" for _ in self.word_being_guessed]

    def place_word(self):
        if self.guessed_word_so_far_label is not None:
            self.guessed_word_so_far_label.pack_forget()
        self.guessed_word_so_far_label = ttk.Label(self, text=self.guessed_word_so_far)
        self.guessed_word_so_far_label.pack()

    def add_letters_to_the_word(self, char):
        "Updates the word with the guessed letters."
        for index, letter in enumerate(self.word_being_guessed):
            if char == letter:
                self.guessed_word_so_far[index] = char
