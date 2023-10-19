import random
import string
import tkinter as tk
from tkinter import ttk

def generate_password(length, use_lower, use_upper, use_digits, use_special):
    character_sets = []

    if use_lower:
        character_sets.append(string.ascii_lowercase)
    if use_upper:
        character_sets.append(string.ascii_uppercase)
    if use_digits:
        character_sets.append(string.digits)
    if use_special:
        character_sets.append(string.punctuation)

    if not character_sets:
        return "Select at least one character set."

    all_chars = ''.join(character_sets)
    
    if length < 8:
        return "Password length must be at least 8 characters."
    
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def generate_password_button():
    length = int(length_entry.get())
    use_lower = lower_var.get()
    use_upper = upper_var.get()
    use_digits = digits_var.get()
    use_special = special_var.get()

    password = generate_password(length, use_lower, use_upper, use_digits, use_special)

    password_label.config(text="Generated Password: " + password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Label and Entry for password length
length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Checkboxes for character sets
lower_var = tk.BooleanVar()
lower_check = ttk.Checkbutton(root, text="Lowercase", variable=lower_var)
lower_check.pack()

upper_var = tk.BooleanVar()
upper_check = ttk.Checkbutton(root, text="Uppercase", variable=upper_var)
upper_check.pack()

digits_var = tk.BooleanVar()
digits_check = ttk.Checkbutton(root, text="Digits", variable=digits_var)
digits_check.pack()

special_var = tk.BooleanVar()
special_check = ttk.Checkbutton(root, text="Special Characters", variable=special_var)
special_check.pack()

# Generate Password button
generate_button = ttk.Button(root, text="Generate Password", command=generate_password_button)
generate_button.pack()

# Label to display generated password
password_label = tk.Label(root, text="")
password_label.pack()

root.mainloop()
