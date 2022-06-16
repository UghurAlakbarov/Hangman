import tkinter as tk
from tkinter import ttk


class Trees(ttk.Label):

    "This class is used to show the current progress via pictures of hanging tree being built"

    image_label = None

    def __init__(self, controller):
        self.controller = controller
        
        self.change_picture()
    
    def change_picture(self):
        if self.image_label is not None:
            self.image_label.destroy()

        self.image = tk.PhotoImage(file=f'assets/tree{self.controller.attempts_used}.png')
        self.image_label = ttk.Label(self.controller, image=self.image)
        self.image_label.pack(side='right')
