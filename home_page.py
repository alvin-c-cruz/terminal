import tkinter as tk

class HomePage(tk.Frame):
    def __init__(self, parent, controller, conn):
        super().__init__(parent)
        
        # Configure the grid to center widgets
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Center the content
        frame = tk.Frame(self)
        frame.grid(row=1, column=0)

        label = tk.Label(frame, text="This is the home page!", font=("Arial", 16))
        label.grid(row=0, column=0, pady=20)

        logout_button = tk.Button(frame, text="Logout", command=lambda: controller.show_frame("LoginPage"))
        logout_button.grid(row=1, column=0, pady=20)
        
        # Close Application Button
        close_button = tk.Button(frame, text="Close Application", command=self.close_app)
        close_button.grid(row=2, column=0, pady=10)

    # Method to close the application
    def close_app(self):
        self.quit()  # Close the application
