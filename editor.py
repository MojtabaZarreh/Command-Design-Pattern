import tkinter as tk
from cmd_pat import Command

class Editor:
    def __init__(self, canvas: tk.Canvas):
        self.canvas = canvas
        self.undo_stack: list[Command] = []
        self.redo_stack: list[Command] = []
        
    def execute(self, command: Command):
        command.do()
        self.undo_stack.append(command)
        self.redo_stack.clear()
        
    def undo(self):
        if self.undo_stack:
            cmd = self.undo_stack.pop()
            cmd.undo()
            self.redo_stack.append(cmd)
    
    def redo(self):
        if self.redo_stack:
            cmd = self.redo_stack.pop()
            cmd.do()
            self.undo_stack.append(cmd)