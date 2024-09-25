import tkinter as tk
from tkinter import messagebox

class RegistrationPage(tk.Frame):
    def __init__(self, parent, controller, conn):
        super().__init__(parent)
        self.controller = controller
        self.conn = conn  # Pass the connection to this page

        # Configure the grid to center widgets
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create a frame to hold the registration form and center it
        frame = tk.Frame(self)
        frame.grid(row=1, column=0)

        label = tk.Label(frame, text="Register", font=("Arial", 16))
        label.grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(frame, text="Username:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.username_entry = tk.Entry(frame)
        self.username_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(frame, text="Password:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.password_entry = tk.Entry(frame, show="*")
        self.password_entry.grid(row=2, column=1, padx=10, pady=5)

        register_button = tk.Button(frame, text="Register", command=self.register)
        register_button.grid(row=3, column=0, columnspan=2, pady=10)

        login_button = tk.Button(self, text="Go to Login", command=lambda: controller.show_frame("LoginPage"))
        login_button.grid(row=4, column=0, pady=5)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        cursor = self.conn.cursor()

        # Check if the username already exists
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            messagebox.showerror("Registration Failed", "Username already exists.")
        elif not username or not password:
            messagebox.showerror("Registration Failed", "Username and password cannot be empty.")
        else:
            # Insert the new user into the database
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            self.conn.commit()
            messagebox.showinfo("Registration Successful", "You have successfully registered!")
            self.controller.show_frame("LoginPage")
