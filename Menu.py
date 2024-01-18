import tkinter
from Button import Button
from FlashGroup import FlashGroup
from FileManagement import *

class Menu:
    def __init__(self, window) -> None:
        self.window = window
        self.variables = []
        self.widgets = {}
        self.flashGroups = loadData()
        self.launchMainMenu()

    def clear(self):
        self.widgets.clear()
        self.variables.clear()
        for widget in self.window.winfo_children():
            widget.destroy()

    def addVariable(self):
        variable = tkinter.StringVar()
        self.variables.append(variable)
        return variable

    def generateEntry(self, name, y, variable):
        border_color = tkinter.Frame(self.window, highlightbackground="purple", highlightthickness=2)

        self.widgets[name] = tkinter.Entry(border_color, textvariable=variable)
        self.widgets[name].configure(bg="black", fg="#ac20fd", width=25, font=('Helvetica', 25), borderwidth=0)
        self.widgets[name].pack()

        border_color.place(relx=0.5, rely=y, anchor="center")

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

    def launchMainMenu(self):
        self.clear()
        self.widgets["add-button"] = Button("+ Add", 0.5, 0.2, 60, 1, self.window)
        self.widgets["add-button"].onClick(lambda: self.launchAddCardGroupMenu())

        def onSelect(event):
            widget = event.widget
            selection = widget.curselection()
            value = widget.get(selection[0])
            for group in self.flashGroups:
                if(group.getName() == value):
                    self.launchCardGroupMenu(group)

        flashGroupString = []
        for flash in self.flashGroups: 
            flashGroupString.append(flash.getName())

        self.generateLists("all-groups-list", flashGroupString)
        self.widgets["all-groups-list"].bind("<Double-Button-1>", onSelect)

    def launchAddCardGroupMenu(self):
        self.clear()

        name = self.addVariable()
        self.generateEntry("name-entry", 0.2, name)

        def addGroup():
            if (name.get() != ""):
                self.flashGroups.append(FlashGroup(name.get()))
                appendFlashGroupData(name.get())
                self.launchMainMenu()

        self.widgets["submit-button"] = Button("Add Group", 0.5, 0.5, 20, 4, self.window)
        self.widgets["submit-button"].onClick(lambda: addGroup())

    """
    Generates the menu for adding a
    new flashcard
    """
    def launchAddFlashCardMenu(self, flashGroup):
        self.clear()

        front, back = self.addVariable(), self.addVariable()
        self.generateEntry("front-entry", 0.2, front)
        self.generateEntry("back-entry", 0.3, back)

        def addFlashCard():
            flashGroup.addFlashCard(front.get(), back.get())
            self.launchCardGroupMenu(flashGroup)

        self.widgets["submit-button"] = Button("Add FlashCard", 0.5, 0.5, 30, 3, self.window)
        self.widgets["submit-button"].onClick(lambda: addFlashCard())
        self.widgets["back-button"] = Button("Back", 0.5, 0.7, 30, 3, self.window)
        self.widgets["back-button"].onClick(lambda: self.launchCardGroupMenu(flashGroup))

    def launchCardGroupMenu(self, flashGroup):
        self.clear()
        self.widgets["run-button"] = Button("Run Flashcards", 0.5, 0.15, 60, 1, self.window)

        self.widgets["add-button"] = Button("+ Add FlashCard", 0.5, 0.8, 60, 1, self.window)
        self.widgets["add-button"].onClick(lambda: self.launchAddFlashCardMenu(flashGroup))

        self.widgets["back-button"] = Button("Back", 0.5, 0.925, 60, 1, self.window)
        self.widgets["back-button"].onClick(lambda: self.launchMainMenu())


        self.generateLists("flashcard-lists", flashGroup.strList())