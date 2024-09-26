import tkinter as tk

# Create a custom Entry widget by inheriting from tk.Entry
class CustomEntry(tk.Entry):
    def __init__(self, master=None, placeholder="Enter text...", *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.default_fg_color = self['fg']  # Save the default text color
        self.insert(0, self.placeholder)
        self['fg'] = 'grey'

        # Bind events for focus in and out
        self.bind("<FocusIn>", self._remove_placeholder)
        self.bind("<FocusOut>", self._add_placeholder)

    def _remove_placeholder(self, event=None):
        if self.get() == self.placeholder:
            self.delete(0, tk.END)
            self['fg'] = self.default_fg_color

    def _add_placeholder(self, event=None):
        if not self.get():
            self.insert(0, self.placeholder)
            self['fg'] = 'grey'

    def clear_content(self):
        self._add_placeholder()

    # Define a property to get and set the value of the Entry widget
    @property
    def value(self):
        # Return the current value, but check if the placeholder is showing
        if self.get() == self.placeholder:
            return ""
        return self.get()

    @value.setter
    def value(self, new_value):
        # Remove placeholder and set new value
        self._remove_placeholder()
        self.delete(0, tk.END)
        self.insert(0, new_value)
        self['fg'] = self.default_fg_color  # Ensure text color is normal
