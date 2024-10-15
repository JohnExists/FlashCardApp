import tkinter

class Button():

    """
    Initializes a new instance of the class.

    @param text The text displayed on the button.
    @param x The horizontal position of the button.
    @param y The vertical position of the button.
    @param width The width of the button.
    @param height The height of the button.
    @param window The window that the button is being displayed on
    """
    def __init__(self, text, x, y, width, height, window) -> None:
        self.button_frame = tkinter.Frame(window, highlightbackground="purple", highlightthickness=2)

        self.button = tkinter.Button(self.button_frame, text=text, width=width, height=height)
        self.button.configure(bg="black", fg="#ac20fd", borderwidth=0, font=('Helvetica', 15), padx=10, pady=10)
        self.button.bind("<Enter>", lambda e: self.button.config(bg="#ac20fd", fg="black"))
        self.button.bind("<Leave>", lambda e: self.button.config(bg="black", fg="#ac20fd"))
        self.button.pack()

        self.button_frame.place(relx=x, rely=y, anchor="center")

    """
    Executes a function once this button has been clicked

    @param action The function thay will be executed on this button click
    """
    def onClick(self, action):
        self.button.configure(command=action)

    """
    Sets the text that displays on the button

    @param newText The new string that will be displayed on the button
    """
    def setText(self, newText):
        self.button.configure(text=newText)
        
