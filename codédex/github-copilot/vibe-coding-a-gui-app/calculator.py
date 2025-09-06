"""
Build a Calculator GUI application using Tkinter.
It should have buttons for digits 0-9, operations (+, -, *, /), and submit (=).
"""
import tkinter as tk
from tkinter import ttk

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x600")
        self.create_widgets()

    def create_widgets(self):
        self.display = ttk.Entry(self, font=("Arial", 24), justify="right")
        self.display.pack(expand=True, fill="both")

        buttons_frame = ttk.Frame(self)
        buttons_frame.pack(expand=True, fill="both")

        # Create buttons for digits and operations
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", "C", "=", "+"
        ]

        for i, button in enumerate(buttons):
            action = lambda x=button: self.on_button_click(x)
            ttk.Button(buttons_frame, text=button, command=action).grid(row=i//4, column=i%4, sticky="nsew")

        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.grid_rowconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == "C":
            self.display.delete(0, tk.END)
        elif char == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            self.display.insert(tk.END, char)

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()