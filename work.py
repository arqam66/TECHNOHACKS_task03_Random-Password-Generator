import tkinter as tk
import random
import string
import pyperclip

def generate_password():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = int(num_letters_entry.get())
    nr_symbols = int(num_symbols_entry.get())
    nr_numbers = int(num_numbers_entry.get())

    password_list = []

    for _ in range(nr_letters):
        password_list.append(random.choice(letters))

    for _ in range(nr_symbols):
        password_list.append(random.choice(numbers))

    for _ in range(nr_numbers):
        password_list.append(random.choice(symbols))

    random.shuffle(password_list)

    password = ''.join(password_list)
    password_display.config(text="Generated Password: " + password)
    pyperclip.copy(password)  # Copy password to clipboard

root = tk.Tk()
root.title("Password Generator")
root.geometry("300x250")

num_letters_label = tk.Label(root, text="Number of Letters:")
num_letters_label.pack()
num_letters_entry = tk.Entry(root)
num_letters_entry.pack()

num_symbols_label = tk.Label(root, text="Number of Symbols:")
num_symbols_label.pack()
num_symbols_entry = tk.Entry(root)
num_symbols_entry.pack()

num_numbers_label = tk.Label(root, text="Number of Numbers:")
num_numbers_label.pack()
num_numbers_entry = tk.Entry(root)
num_numbers_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_display = tk.Label(root, text="")
password_display.pack()

root.mainloop()
