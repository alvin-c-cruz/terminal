import tkinter as tk
from tkinter import messagebox
from custom_entry import CustomEntry
import bcrypt


class LoginPage(tk.Frame):
    def __init__(self, parent, controller, conn):
        super().__init__(parent)
        self.controller = controller
        self.conn = conn  # Pass the connection to this page

        # Configure grid to center the login frame in the middle
        self.grid_columnconfigure(0, weight=1)

        # Create a frame to hold the login form and center it
        login_frame = tk.Frame(self)
        login_frame.grid(row=1, column=0, padx=20, pady=20)

        # # Center the form inside the frame
        # login_frame.grid_columnconfigure(0, weight=1)
        # login_frame.grid_columnconfigure(1, weight=1)

        # Login label
        label = tk.Label(login_frame, text="Login", font=("Arial", 16))
        label.grid(row=0, column=0, columnspan=2, pady=10)

        # Username label and entry
        tk.Label(login_frame, text="Username:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.username_entry = CustomEntry(login_frame)
        self.username_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        self.username_entry.bind("<Return>", lambda event: self.login())
        self.username_entry.value = "admin"

        # Password label and entry
        tk.Label(login_frame, text="Password:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.password_entry = CustomEntry(login_frame, show="*")
        self.password_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        self.password_entry.bind("<Return>", lambda event: self.login())
        self.password_entry.value = "ac1123581321"

        # Login button
        login_button = tk.Button(login_frame, text="Login", command=self.login)
        login_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Register button below the login form
        register_button = tk.Button(self, text="Go to Registration", command=lambda: controller.show_frame("RegistrationPage"))
        register_button.grid(row=2, column=0, pady=10)

    def login(self):
        username = self.username_entry.get()
        entered_password = self.password_entry.get()

        cursor = self.conn.cursor()

        # Query the database to check if the username and password match
        cursor.execute("SELECT * FROM users WHERE username = ?", (username, ))
        user = cursor.fetchone()

        if user:
            if bcrypt.checkpw(entered_password.encode('utf-8'), user['password']):
                self.username_entry.clear_content()
                self.password_entry.clear_content()

                self.controller.show_frame("HomePage")
                return

        messagebox.showerror("Login Failed", "Invalid username or password.")
