import tkinter as tk
from tkinter import ttk


class Trees(ttk.Frame):

    "This class is used to show the current progress via pictures of hanging tree being built"

    image_label = None

    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.change_picture()
    
    def change_picture(self):
        if self.image_label is not None:
            self.image_label.destroy()

        self.image = tk.PhotoImage(file=f'assets/tree{self.master.attempts_used}.png')
        self.image_label = ttk.Label(self, image=self.image)
        self.image_label.pack()
