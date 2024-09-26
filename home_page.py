import tkinter as tk

class HomePage(tk.Frame):
    def __init__(self, parent, controller, conn):
        super().__init__(parent)
        
        self.controller = controller

        # # Configure the grid to center widgets
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(0, weight=1)

        # Center the content
        self.frame = tk.Frame(self)
        self.frame.grid(row=1, column=0, padx=60)


        # Define the pixel size for 1x1 inch buttons assuming 96 DPI
        button_size_px = 96  # 1 inch = 96 pixels

        # Create a 4x4 grid of buttons with 1x1 inch size
        buttons = [
            ("Button 1", None),
            ("Button 2", None),
            ("Button 3", None),
            ("Button 4", None),
            ("Button 5", None),
            ("Button 6", None),
            ("Button 7", None),
            ("Button 8", None),
            ("Button 9", None),
            ("Button 10", None),
            ("Button 11", None),
            ("Button 12", None),
            ("Button 13", None),
            ("Button 14", None),
            ("Button 15", None),
            ("Button 16", None),
            ("Button 17", None),
            ("Button 18", None),
            ("Button 19", None),
            ("Button 20", None),
            ("Button 21", None),
            ("Button 22", None),
            ("Button 23", None),
            ("Button 24", None),
            ("Button 25", None),
            ("Button 26", None),
            ("Button 27", None),
            ("Button 28", None),
            ("Button 29", None),
            ("Button 30", None),
            ("Button 31", None),
            ("Button 32", None),
            ("Button 33", None),
            ("Button 34", None),
            ("Button 35", None),
            ("Button 36", None),
            ("Button 37", None),
            ("Button 38", None),
            ("Button 39", None),
            ("Button 40", None),
            ("Button 41", None),
            ("Button 42", None),
            ("Button 43", None),
            ("Button 44", None),
            ("Button 45", None),
            ("Button 46", None),
            ("Button 47", None),
            ("Logout", lambda: controller.show_frame("LoginPage")),
            ("Close\nApplication", self.close_app)
        ]

        # Place buttons in a 4x4 grid with size 1x1 inch
        for i, (btn_text, command) in enumerate(buttons):
            row = i // 7 + 2  # Start placing buttons from row 2
            col = i % 7
            button = tk.Button(self.frame, text=btn_text, command=command, width=button_size_px//10, height=button_size_px//20)
            button.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

        # Configure grid to ensure buttons are evenly distributed
        for i in range(4):
            self.frame.grid_columnconfigure(i, weight=1)
        for i in range(4):
            self.frame.grid_rowconfigure(i + 2, weight=1)

    def close_app(self):
        self.quit()  # Close the application
