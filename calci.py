import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")
        
        self.expression = ""
        
        # Entry widget to display expressions and results
        self.display = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, ipady=10)
        
        # Create calculator buttons
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", "C", "=", "+"
        ]
        
        # Position buttons in a grid layout
        row, col = 1, 0
        for button_text in buttons:
            button = tk.Button(root, text=button_text, font=("Arial", 18), width=5, height=2,
                               command=lambda text=button_text: self.on_button_click(text))
            button.grid(row=row, column=col, padx=5, pady=5)
            
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, char):
        if char == "=":
            self.calculate()
        elif char == "C":
            self.clear()
        else:
            self.expression += str(char)
            self.update_display()

    def calculate(self):
        try:
            result = eval(self.expression)
            self.expression = str(result)
            self.update_display()
        except Exception:
            messagebox.showerror("Error", "Invalid Expression")
            self.clear()

    def clear(self):
        self.expression = ""
        self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()