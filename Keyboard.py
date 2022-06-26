import tkinter as tk
from tkinter import ttk


class Keyboard(ttk.Frame):

    "The keyboard"

    def __init__(self, master):
        super().__init__(master)

        letter : str
        self.master = master

        # Creates buttons for each letter
        self.letters = {}
        for letter in "QWERTYUIOPASDFGHJKLZXCVBNM":
            self.letters[letter] = ttk.Button(
                self,
                text=f'{letter}',
                width=6,
                command=lambda letter=letter : self.virtual_keyboard_key_press(letter)
            )
            self.focus_set()
            self.bind('<Key>', self.physical_keyboard_key_input)
        
        # Puts buttons in a grid linewise
        for index, letter in enumerate("QWERTYUIOP"):
            self.letters[letter].grid(row=1, column=index, ipadx=6, ipady=10)
        for index, letter in enumerate("ASDFGHJKL"):
            self.letters[letter].grid(row=2, column=index, ipadx=6, ipady=10)
        for index, letter in enumerate("ZXCVBNM"):
            self.letters[letter].grid(row=3, column=index, ipadx=6, ipady=10)
    
    def virtual_keyboard_key_press(self, letter):
        self.master.letter_input(letter)
    
    def physical_keyboard_key_input(self, event : tk.Event=None):
        letter = event.char.upper()
        self.master.letter_input(letter)
