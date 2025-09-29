# Undo/Redo Drawing Editor

A Python Tkinter application demonstrating the **Command design pattern** with **undo/redo functionality**. This project shows how to structure user actions as objects, maintain execution history, and manipulate a canvas efficiently.


https://github.com/user-attachments/assets/6893602e-0ad2-44a3-9237-2aa3834c22c0


## Overview

Users can draw **circles** and **rectangles** on a canvas and undo or redo their actions. The focus of this project is on:

- **Software design principles**
- **Data structures** for action history
- Separation of **GUI and business logic**

## Features

- Draw random **circles** and **rectangles**
- **Undo** the last executed action
- **Redo** previously undone actions
- Clean separation of concerns using the **Command pattern**
- Easily extendable for new commands or shapes

## Technical Details

### Command Pattern

The **Command pattern** encapsulates every user action as an object:

- Each action implements an interface with `do` and `undo` operations.
- The GUI triggers commands without knowing their internal implementation.
- Commands store all necessary data to execute and reverse an action.

### DrawShapeCommand

- Represents a drawing action (circle or rectangle).
- Stores the shape type, coordinates, options (like color), and a reference to the canvas item.
- Supports both execution and reversal of the action.

### Editor: Undo/Redo Management

The `Editor` class manages two **stacks**:

1. **Undo stack** – stores executed commands.
2. **Redo stack** – stores undone commands.

**Flow:**

- **Execute a command:** perform action → push to undo stack → clear redo stack.
- **Undo:** pop from undo stack → reverse action → push to redo stack.
- **Redo:** pop from redo stack → re-execute action → push back to undo stack.

**Benefits:**

- Undo/redo operations have **constant time complexity**.
- History of actions is preserved, enabling unlimited undo/redo (memory permitting).
- Commands can be added or extended without modifying the editor logic.

### Data Structures

- **Stacks** (`list`) maintain history efficiently.
- Each command object is self-contained, holding all data needed for execution and reversal.
- Ensures **loose coupling** between GUI and business logic.

<img width="3622" height="2697" alt="b651c92b-96b4-4a68-ba35-02f32753fbf0_Copy_of_6-4_UndoRedoStacks" src="https://github.com/user-attachments/assets/7f01e0e3-4c40-41a6-b891-f36956311acb" />
