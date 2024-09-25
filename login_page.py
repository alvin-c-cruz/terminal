import tkinter as tk
from tkinter import messagebox

class LoginPage(tk.Frame):
    def __init__(self, parent, controller, conn):
        super().__init__(parent)
        self.controller = controller
        self.conn = conn  # Pass the connection to this page

        # Configure the grid to center widgets
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create a frame to hold the login form and center it
        frame = tk.Frame(self)
        frame.grid(row=1, column=0)

        label = tk.Label(frame, text="Login", font=("Arial", 16))
        label.grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(frame, text="Username:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.username_entry = tk.Entry(frame)
        self.username_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(frame, text="Password:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.password_entry = tk.Entry(frame, show="*")
        self.password_entry.grid(row=2, column=1, padx=10, pady=5)

        login_button = tk.Button(frame, text="Login", command=self.login)
        login_button.grid(row=3, column=0, columnspan=2, pady=10)

        register_button = tk.Button(self, text="Go to Registration", command=lambda: controller.show_frame("RegistrationPage"))
        register_button.grid(row=4, column=0, pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        cursor = self.conn.cursor()

        # Query the database to check if the username and password match
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()

        if user:
            messagebox.showinfo("Login Successful", "You are now logged in!")
            self.controller.show_frame("HomePage")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
