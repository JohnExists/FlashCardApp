import tkinter
from Button import Button
from FileManagement import *

class MenuContainer:
    """
    Initializes a new instance of the class.

    @param window The main application window.
    """
    def __init__(self, window) -> None:
        self.window = window
        self.variables = []
        self.widgets = {}
        self.flashGroups = loadData()

    """
    Clears all widgets and associated variables from the current window.
    """
    def clear(self):
        self.widgets.clear()
        self.variables.clear()
        for widget in self.window.winfo_children():
            widget.destroy()

    """
    Adds a new string variable to the list of variables.

    @param value The initial value for the StringVar (default is an empty string).
    @returns The created StringVar instance.
    """
    def addVariable(self, value=""):
        variable = tkinter.StringVar(value=value)
        self.variables.append(variable)
        return variable

    """
    Generates an entry widget with a specified name, position, and text variable.

    @param name The identifier for the entry widget.
    @param y The vertical position (relative to the window) of the entry widget between (0 and 1).
    @param variable The Tkinter variable associated with the entry widget, 
                     which holds the text input.
    """
    def generateEntry(self, name, y, variable):
        border_color = tkinter.Frame(self.window, highlightbackground="purple", highlightthickness=2)

        self.widgets[name] = tkinter.Entry(border_color, textvariable=variable)
        self.widgets[name].configure(bg="black", fg="#ac20fd", width=40, font=('Helvetica', 25), borderwidth=0)
        self.widgets[name].pack()

        border_color.place(relx=0.5, rely=y, anchor="center")

    """
    Creates a list object, each option is a string that is stacked above one another
    These options can be treated as a button if the user wishes

    @param name The identifier for the list box widget.
    @param list The list of strings to display in the list box.
    """
    def generateLists(self, name, list):
        # Draws the purple border
        border_color = tkinter.Frame(self.window, highlightbackground="purple", highlightthickness=2)
        
        # Initializes and places the scrollbar on the right
        scrollbar = tkinter.Scrollbar(border_color)
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        # Creates the list box of all the card groups available
        listBox = tkinter.Listbox(border_color, yscrollcommand=scrollbar.set)
        listBox.configure(background="black", foreground="purple",
                          font=('Helvetica', 25), width=35, height=6, borderwidth=0)
        for item in list:
            listBox.insert(tkinter.END, item)


        # Places the border, and list box in the center of the screen
        border_color.place(relx=0.5, rely=0.5, anchor="center")

        # Packs the list box in the border
        listBox.pack()
        # Adds it to the widget list
        self.widgets[name] = listBox
        # Attaches the scroll bar to the list box
        scrollbar.config(command=listBox.yview)

    """
    Allows a function to be executed once a list option has
    been double-clicked by the user

    @param name The identifier for the list object widget.
    @param command The function to be called when the list box is double-clicked.
    """
    def setListsOnDoubleClick(self, name, command):
        self.widgets[name].bind("<Double-Button-1>", command)

    """
    Creates a button and adds it to the widget list.

    @param name The identifier for the button widget.
    @param buttonTitle The text displayed on the button.
    @param x The horizontal position of the button.
    @param y The vertical position of the button.
    @param width The width of the button.
    @param height The height of the button.
    """
    def createButton(self, name, buttonTitle, x, y, width, height):
        self.widgets[name] = Button(buttonTitle, x, y, width, height, self.window)

    """
    Sets the click event handler for a specified button.

    This method associates a function to be called when the button 
    identified by the given name is clicked.

    @param name The identifier for the button widget.
    @param onClick The function to be called when the button is clicked.
    """
    def setButtonOnClick(self, name, onClick):
        self.widgets[name].onClick(onClick)

    def flashGroupsToString(self):
        result = []
        for flash in self.flashGroups: 
            result.append(flash.getName())
        return result