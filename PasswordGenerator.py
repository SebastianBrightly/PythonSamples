import random
import string
import tkinter as tk
from ttkthemes import ThemedTk

def generate_password():
    length = int(length_entry.get())
    use_uppercase = uppercase_var.get()
    use_digits = digits_var.get()
    use_special_chars = special_chars_var.get()

    chars = string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    generated_password.set(password)

# Create the ThemedTk window
window = ThemedTk(theme="arc")  # You can change the theme (e.g., "scidgrey")

window.title("Password Generator")

# Widgets for password generation options
length_label = tk.Label(window, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(window)
length_entry.pack()

uppercase_var = tk.BooleanVar()
uppercase_check = tk.Checkbutton(window, text="Include Uppercase", variable=uppercase_var)
uppercase_check.pack()

digits_var = tk.BooleanVar()
digits_check = tk.Checkbutton(window, text="Include Digits", variable=digits_var)
digits_check.pack()

special_chars_var = tk.BooleanVar()
special_chars_check = tk.Checkbutton(window, text="Include Special Characters", variable=special_chars_var)
special_chars_check.pack()

# Create a rounded button for generating passwords
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

# Widget to display the generated password
generated_password = tk.StringVar()
generated_password_label = tk.Label(window, textvariable=generated_password)
generated_password_label.pack()

# Run the main loop
window.mainloop()
