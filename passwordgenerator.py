import tkinter as tk
import random
import string


def generate_password():
    try:
        password_length = int(entry_length.get())
        if password_length <= 0:
            generate_button.config(text="Invalid length!")
            return
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_length))
        generated_password_entry.delete(0, tk.END)
        generated_password_entry.insert(0, password)
    except ValueError:
        generate_button.config(text="GENERATE PASSWORD")


def reset_fields():
    entry_length.delete(0, tk.END)
    generated_password_entry.delete(0, tk.END)
    name.delete(0, tk.END)


# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("900x630+270+100")
# Create a frame to hold widgets
frame = tk.Frame(root)
frame.pack()

title = tk.Label(frame, text="Password Generator", font=("ariel", 28, 'underline', 'bold'), fg="blue")
title.grid(row=0, columnspan=50)

user_name = tk.Label(frame, text="Enter user name:", font=('ariel', 17))
user_name.grid(row=1, column=1, padx=2, pady=60)

name = tk.Entry(frame, font=('ariel', 15), bd=5)
name.grid(row=1, column=2, padx=40)

# Label for instructions
length = tk.Label(frame, text="Enter password length:", font=('ariel', 17))
length.grid(row=2, column=1)

# Entry for password length
entry_length = tk.Entry(frame,font=('ariel', 15), bd=5)
entry_length.grid(row=2, column=2)

length = tk.Label(frame, text="Generated Password:", font=('ariel', 17))
length.grid(row=3, column=1)

# Entry to display generated password
generated_password_entry = tk.Entry(frame, font=('ariel', 15), bd=5)
generated_password_entry.grid(row=3, column=2, pady=60)

# Button to generate password
generate_button = tk.Button(frame, text="GENERATE PASSWORD", command=generate_password, width=30, height=1, bg='blue',
                            fg='white', font=('ariel', 18, 'bold'), bd=0, border=5, highlightcolor='black')
generate_button.grid(row=4, column=2)

# Accept button
accept_button = tk.Button(frame, text="ACCEPT",  width=10, height=2, bd=5, bg='white', fg='blue')
accept_button.grid(row=5, column=2, pady=10)

# Reset button
reset_button = tk.Button(frame, text="RESET", command=reset_fields, width=10, height=2, bd=5, bg='white', fg='blue')
reset_button.grid(row=6, column=2, pady=10)


# Run the application
root.mainloop()
