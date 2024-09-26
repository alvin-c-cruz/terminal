import tkinter as tk
from user.login_page import LoginPage
from user.registration_page import RegistrationPage
from home_page import HomePage
from extensions import init_db, get_db_connection

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("RIC Inventory")

        # Initialize the database and keep the connection open
        init_db()
        self.conn = get_db_connection()

        # Initialize container to hold the different frames
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        # Dictionary to hold the different pages
        self.frames = {}

        for F in (LoginPage, RegistrationPage, HomePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self, conn=self.conn)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def on_closing(self):
        # Close the database connection before closing the app
        self.conn.close()
        self.quit()

if __name__ == "__main__":
    app = App()

    # Bind the window's close event to close the database connection
    app.protocol("WM_DELETE_WINDOW", app.on_closing)

    app.mainloop()
