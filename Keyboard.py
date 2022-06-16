from tkinter import ttk


class Keyboard(ttk.Frame):

    "The keyboard"

    def __init__(self, container):

        super().__init__(container)

        letter : str
        self.container = container

        # Creates buttons for each letter
        self.letters = {}
        for letter in "QWERTYUIOPASDFGHJKLZXCVBNM":
            self.letters[letter] = ttk.Button(
                self,
                text=f'{letter}',
                width=6,
                command=lambda letter=letter : self.letter_pushed(letter)
            )
        
        # Puts buttons in a grid linewise
        for index, letter in enumerate("QWERTYUIOP"):
            self.letters[letter].grid(row=1, column=index, ipadx=6, ipady=10)
        for index, letter in enumerate("ASDFGHJKL"):
            self.letters[letter].grid(row=2, column=index, ipadx=6, ipady=10)
        for index, letter in enumerate("ZXCVBNM"):
            self.letters[letter].grid(row=3, column=index, ipadx=6, ipady=10)
    
    def letter_pushed(self, letter):
        self.container.letter_input(letter)
