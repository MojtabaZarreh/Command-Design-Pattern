import tkinter as tk
from dataclasses import dataclass
from cmd_pat import Command


@dataclass
class DrawShapeCommand(Command):
    canvas: tk.Canvas
    coords: tuple
    shape: str
    options: dict
    item: int = None

    def do(self):
        draw_fn = {
            "circle": lambda: self.canvas.create_oval(*self.coords, **self.options),
            "rect": lambda: self.canvas.create_rectangle(*self.coords, **self.options),
        }[self.shape]
        self.item = draw_fn()

    def undo(self):
        if self.item:
            self.canvas.delete(self.item) 