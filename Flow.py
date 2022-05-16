import tkinter as tk
import Utility as ut
from Presentation import Presentation
from Button import Button
from Text import Text
from Image import Image

class Flow:
    def __init__(self):
        print("Main Flow Initialized")

    def start(self, canvas: Presentation):
        print("Hello there person reading the console :)")

        self.canvas = canvas
        self.canvas.configure(bg='black')
        mb = Button(canvas, 0, 0, 100, 100, onclick=print)
        mb.move_easeinout_to((1503, 855), show=True)
        mb.move_easeinout_to((1467, 745), show=True)
        mb.move_easeinout_to(mb.get_vh_centre())