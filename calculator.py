import tkinter as tk
from tkinter import messagebox

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()

    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 == 0:
            messagebox.showerror("Error", "Cannot divide by zero!")
            return
        result = num1 / num2

    messagebox.showinfo("Result", f"The result is: {result}")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Number entry fields
label_num1 = tk.Label(window, text="Enter first number:")
label_num1.grid(row=0, column=0)
entry_num1 = tk.Entry(window)
entry_num1.grid(row=0, column=1)

label_num2 = tk.Label(window, text="Enter second number:")
label_num2.grid(row=1, column=0)
entry_num2 = tk.Entry(window)
entry_num2.grid(row=1, column=1)

# Operation selection
label_operation = tk.Label(window, text="Select operation:")
label_operation.grid(row=2, column=0)
operation_var = tk.StringVar()
operation_choices = ["Addition", "Subtraction", "Multiplication", "Division"]
operation_var.set(operation_choices[0])
operation_menu = tk.OptionMenu(window, operation_var, *operation_choices)
operation_menu.grid(row=2, column=1)

# Button to calculate
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=3, columnspan=2)

# Run the main event loop
window.mainloop()
