import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.expression = ""

        # Set window background color
        self.root.configure(bg="#e0f7fa")

        # Create display widget
        self.display = tk.Entry(root, font=('Arial', 24), borderwidth=0, relief="flat", bg="#e0f7fa")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Create buttons
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        button_style = {
            "font": ('Arial', 18),
            "bg": "#b3e5fc",
            "fg": "#01579b",
            "borderwidth": 0,
            "relief": "flat",
            "width": 5,
            "height": 2
        }

        for (text, row, col) in buttons:
            if text == "=":
                tk.Button(self.root, text=text, command=self.calculate, **button_style).grid(
                    row=row, column=col, sticky="nsew", padx=5, pady=5)
            else:
                tk.Button(self.root, text=text, command=lambda b=text: self.click(b), **button_style).grid(
                    row=row, column=col, sticky="nsew", padx=5, pady=5)

    def click(self, item):
        if item == "C":
            self.expression = ""
        else:
            self.expression += str(item)
        self.update_display()

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.expression = result
        except:
            self.expression = "ERROR"
        self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
