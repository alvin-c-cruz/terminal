import tkinter as tk
import win32print
import os

# Constants
TARGET_PRINTER_NAME = "EPSON L120 Series"  # Set your target printer name here
WINDOW_TITLE = "Multiple Page Application"
WINDOW_SIZE = "400x300"
SUGGESTION_LIST = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi', 'lemon', 'mango', 'orange', 'peach', 'pear', 'plum']

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title(WINDOW_TITLE)
        self.root.geometry(WINDOW_SIZE)

        # Frame container to hold different pages
        self.frame_container = tk.Frame(root)
        self.frame_container.pack(fill="both", expand=True)

        # Initialize pages dictionary
        self.pages = {}

        # Show the first page (AutoCompletePage)
        self.show_page(AutoCompletePage)

    def show_page(self, page_class):
        """Destroy the current page and display the new one."""
        # Remove current page if it exists
        for page in self.pages.values():
            page.pack_forget()

        # Create the new page if it hasn't been created yet
        if page_class not in self.pages:
            self.pages[page_class] = page_class(self.frame_container, self)

        # Show the new page
        self.pages[page_class].pack(fill="both", expand=True)


class AutoCompletePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Configure grid for better alignment
        self.grid_columnconfigure(0, weight=1)

        # Entry widget for autocomplete
        self.entry = tk.Entry(self, width=30)
        self.entry.grid(pady=10, padx=20, row=0, column=0, sticky="ew")
        self.entry.bind('<KeyRelease>', self.check_key)

        # Initialize the Listbox (but don't pack it yet)
        self.listbox = None

        # Another entry widget
        self.other = tk.Entry(self, width=30)
        self.other.grid(pady=10, padx=20, row=2, column=0, sticky="ew")

        # Print button
        self.print_button = tk.Button(self, text="Print", command=self.print_text)
        self.print_button.grid(pady=10, padx=20, row=3, column=0, sticky="ew")

        # Button to switch to another page
        self.switch_button = tk.Button(self, text="Go to Another Page", command=lambda: controller.show_page(OtherPage))
        self.switch_button.grid(pady=10, padx=20, row=4, column=0, sticky="ew")

    def create_listbox(self):
        """Create the listbox if it doesn't exist."""
        if self.listbox is None:
            self.listbox = tk.Listbox(self, height=5)
            self.listbox.grid(pady=10, padx=20, row=1, column=0, sticky="ew")
            self.listbox.bind('<<ListboxSelect>>', self.fill_entry)

    def check_key(self, event):
        """Update the listbox based on the user's input."""
        typed_text = self.entry.get()

        # Clear the listbox (or create it if it's destroyed)
        if self.listbox is not None:
            self.listbox.delete(0, tk.END)
        else:
            self.create_listbox()

        # If the typed text is empty, hide the listbox
        if typed_text == '':
            if self.listbox is not None:
                self.listbox.grid_remove()  # Hide the listbox when the entry is empty
            return

        # Display matching suggestions
        for item in SUGGESTION_LIST:
            if typed_text.lower() in item.lower():
                self.listbox.insert(tk.END, item)
        
        # Ensure the listbox is visible
        if self.listbox.size() > 0:
            self.listbox.grid()  # Re-show the listbox if it has items

    def fill_entry(self, event):
        """Fill the entry with the selected suggestion from the listbox."""
        if self.listbox.curselection():
            selected_item = self.listbox.get(self.listbox.curselection())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, selected_item)
            self.listbox.destroy()  # Destroy the listbox after selection
            self.listbox = None  # Set it to None so it can be recreated later

    def print_text(self):
        """Send the selected text to the specific printer."""
        text_to_print = self.entry.get()

        if text_to_print:
            # Get all available printers
            printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS)

            # Look for the specific printer (TARGET_PRINTER_NAME)
            printer_to_use = None

            for printer in printers:
                if printer[2] == TARGET_PRINTER_NAME:
                    printer_to_use = printer
                    break

            if printer_to_use:
                print(f"Printing to {printer_to_use[2]}")

                # Start the print job
                hPrinter = win32print.OpenPrinter(printer_to_use[2])
                try:
                    # Define document info
                    hJob = win32print.StartDocPrinter(hPrinter, 1, ("Print Job", None, "RAW"))
                    win32print.StartPagePrinter(hPrinter)

                    # Send the text data to the printer
                    win32print.WritePrinter(hPrinter, text_to_print.encode("utf-8"))

                    win32print.EndPagePrinter(hPrinter)
                    win32print.EndDocPrinter(hPrinter)
                finally:
                    # Close the printer handle
                    win32print.ClosePrinter(hPrinter)
            else:
                print(f"Printer '{TARGET_PRINTER_NAME}' not found!")
        else:
            print("No text to print!")


class OtherPage(tk.Frame):
    """A simple placeholder for another page."""
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="This is another page!")
        label.pack(pady=20)

        # Button to return to AutoCompletePage
        back_button = tk.Button(self, text="Go back to AutoComplete Page", command=lambda: controller.show_page(AutoCompletePage))
        back_button.pack()


# Main function to run the Tkinter app
def main():
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
