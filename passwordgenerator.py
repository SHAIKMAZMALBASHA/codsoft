import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            messagebox.showerror("Error", "Password length must be a positive integer.")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for password length.")
        return

    password_characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.choice(password_characters) for i in range(length))

    messagebox.showinfo("Generated Password", f"Your generated password is:\n{generated_password}")

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Length entry field
label_length = tk.Label(window, text="Enter password length:")
label_length.grid(row=0, column=0)
entry_length = tk.Entry(window)
entry_length.grid(row=0, column=1)

# Button to generate password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.grid(row=1, columnspan=2)

# Run the main event loop
window.mainloop()
