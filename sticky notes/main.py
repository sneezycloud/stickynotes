import tkinter as tk
from tkinter import simpledialog

class StickyNoteApp:
    def __init__(self):
        self.notes = []

    def create_note(self):
        note = StickyNote()
        self.notes.append(note)

class StickyNote:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Sticky Note")
        self.window.geometry("200x150")
        self.window.configure(bg="#fffb96")
        self.window.overrideredirect(True)  # Removes the window frame
        
        # Text area
        self.text = tk.Text(self.window, wrap=tk.WORD, bg="#fffb96", fg="black", font=("Arial", 12))
        self.text.pack(fill=tk.BOTH, expand=True)

        # Dragging functionality
        self.window.bind("<Button-1>", self.start_move)
        self.window.bind("<B1-Motion>", self.do_move)

        # Close button
        close_btn = tk.Button(self.window, text="X", command=self.close, bg="#ff6766", fg="white", font=("Arial", 10, "bold"))
        close_btn.place(x=175, y=5)

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.window.winfo_x() + deltax
        y = self.window.winfo_y() + deltay
        self.window.geometry(f"+{x}+{y}")

    def close(self):
        self.window.destroy()

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    app = StickyNoteApp()

    # Add a button to create new sticky notes
    while True:
        answer = simpledialog.askstring("Sticky Notes", "Enter 'new' to create a sticky note or 'quit' to exit:")
        if answer == "new":
            app.create_note()
        elif answer == "quit":
            break

    root.mainloop()

if __name__ == "__main__":
    main()
