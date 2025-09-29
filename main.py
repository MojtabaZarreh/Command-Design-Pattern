import tkinter as tk
from draw_shape import DrawShapeCommand
from editor import Editor
import random

def main():
    root = tk.Tk()
    root.title("Undo/Redo")

    canvas = tk.Canvas(root, width=600, height=400, bg="white")
    canvas.pack()

    editor = Editor(canvas)

    def draw_circle():
        x, y = random.randint(50, 550), random.randint(50, 350)
        r = 30
        editor.execute(DrawShapeCommand(
            canvas,
            (x - r, y - r, x + r, y + r),
            "circle",
            {"fill": "blue"}
        ))

    def draw_rect():
        x, y = random.randint(60, 540), random.randint(40, 360)
        w, h = 60, 40
        editor.execute(DrawShapeCommand(
            canvas,
            (x - w // 2, y - h // 2, x + w // 2, y + h // 2),
            "rect",
            {"fill": "red"}
        ))

    frame = tk.Frame(root)
    frame.pack(pady=10)

    for text, cmd in {
        "Draw Circle": draw_circle,
        "Draw Rectangle": draw_rect,
        "Undo": editor.undo,
        "Redo": editor.redo,
    }.items():
        tk.Button(frame, text=text, command=cmd).pack(side=tk.LEFT, padx=5)

    root.mainloop()

if __name__ == "__main__":
    main()