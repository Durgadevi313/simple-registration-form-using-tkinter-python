import tkinter as tk
from tkinter import messagebox

# Function to handle the registration process
def register():
    username = entry_username.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()

    if not username or not password or not confirm_password:
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    messagebox.showinfo("Success", "Registration Successful!")

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Create and place the labels and entry widgets
tk.Label(root, text="Username").grid(row=0, column=0, padx=10, pady=10)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Password").grid(row=1, column=0, padx=10, pady=10)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Confirm Password").grid(row=2, column=0, padx=10, pady=10)
entry_confirm_password = tk.Entry(root, show="*")
entry_confirm_password.grid(row=2, column=1, padx=10, pady=10)

# Create and place the register button
register_button = tk.Button(root, text="Register", command=register)
register_button.grid(row=3, columnspan=2, pady=20)

# Run the main event loop
root.mainloop()
