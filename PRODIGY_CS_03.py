import tkinter as tk
from tkinter import messagebox
import re

# Function to check the password complexity
def check_password():
    password = entry.get()
    complexity_score = 0
    complexity_requirements = {
        "length": len(password) >= 8,
        "uppercase": re.search(r'[A-Z]', password),
        "lowercase": re.search(r'[a-z]', password),
        "digit": re.search(r'\d', password),
        "special_char": re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
    }

    for key, requirement in complexity_requirements.items():
        if requirement:
            complexity_score += 1

    # Assess the complexity score
    if complexity_score == 5:
        result_label.config(text="Password is Strong", fg="#00FF00")
    elif 3 <= complexity_score < 5:
        result_label.config(text="Password is Medium", fg="#FFD700")
    else:
        result_label.config(text="Password is Weak", fg="#FF4500")

# Function to center the window
def center_window(root, width=400, height=200):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    root.geometry(f'{width}x{height}+{x}+{y}')

# Setting up the GUI with a dark-green "hacker" theme
root = tk.Tk()
root.title("Password Complexity Checker")

# Center the window and set a larger size
center_window(root, width=500, height=300)

# Dark-green hacker theme styling
bg_color = "#0A0F0A"  # Dark green background
fg_color = "#00FF00"  # Green text color (hacker style)
entry_bg_color = "#1E5128"  # Lighter green for entry background

# Configure window background
root.configure(bg=bg_color)

# Creating input fields and labels with hacker theme
label = tk.Label(root, text="Enter your password:", fg=fg_color, bg=bg_color, font=("Courier", 14))
label.pack(pady=20)

entry = tk.Entry(root, show="*", width=40, fg=fg_color, bg=entry_bg_color, insertbackground=fg_color, font=("Courier", 14))
entry.pack(pady=10)

check_button = tk.Button(root, text="Check Password", command=check_password, width=20, bg=entry_bg_color, fg=fg_color, font=("Courier", 12), activebackground="#2E8B57")
check_button.pack(pady=20)

result_label = tk.Label(root, text="", fg=fg_color, bg=bg_color, font=("Courier", 14))
result_label.pack(pady=10)

# Start the GUI loop
root.mainloop()
