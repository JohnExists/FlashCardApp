import tkinter


class Button():

    def __init__(self, text, x, y, width, height, window) -> None:
        self.button_frame = tkinter.Frame(window, highlightbackground="purple", highlightthickness=2)

        self.button = tkinter.Button(self.button_frame, text=text, width=width, height=height)
        self.button.configure(bg="black", fg="#ac20fd", borderwidth=0, font=('Helvetica', 15), padx=10, pady=10)
        self.button.bind("<Enter>", lambda e: self.button.config(bg="#ac20fd", fg="black"))
        self.button.bind("<Leave>", lambda e: self.button.config(bg="black", fg="#ac20fd"))
        self.button.pack()

        self.button_frame.place(relx=x, rely=y, anchor="center")

    def center(self):
        self.button_frame.place(relx=0.5, rely=0.5, anchor="center")

    def alignText(self, anchor):
        self.button.configure(anchor=anchor)

    def onClick(self, action):
        self.button.configure(command=action)
