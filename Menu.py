import tkinter
from Button import Button


class Menu:
    def __init__(self, window) -> None:
        self.window = window
        self.variables = []
        self.widgets = {}
        self.flashGroups = []
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
        border_color = tkinter.Frame(self.window, highlightbackground="purple", highlightthickness=2)
        scrollbar = tkinter.Scrollbar(border_color)
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        listBox = tkinter.Listbox(border_color, yscrollcommand=scrollbar.set)
        for item in list:
            listBox.insert(tkinter.END, item)

        border_color.place(relx=0.5, rely=0.5, anchor="center")
        listBox.configure(background="black", foreground="purple",
                          font=('Helvetica', 15), width=60, borderwidth=0)
        listBox.pack()
        self.widgets[name] = listBox

        scrollbar.config(command=listBox.yview)

    def launchMainMenu(self):
        self.clear()
        self.widgets["add-button"] = Button("+ Add", 0.5, 0.2, 60, 1, self.window)
        self.widgets["add-button"].onClick(lambda: self.launchAddMenu())

        def onSelect(event):
            widget = event.widget
            selection = widget.curselection()
            value = widget.get(selection[0])
            print("selection:", selection, ": '%s'" % value)


        self.generateLists("all-groups-list", self.flashGroups)
        self.widgets["all-groups-list"].bind("<Double-Button-1>", onSelect)


    def launchAddMenu(self):
        self.clear()

        name = self.addVariable()
        self.generateEntry("name-entry", 0.2, name)

        def addGroup():
            if (name.get() != ""):
                self.flashGroups.append(name.get())
                self.launchMainMenu()

        self.widgets["submit-button"] = Button("Add Group", 0.5, 0.5, 20, 4, self.window)
        self.widgets["submit-button"].onClick(lambda: addGroup())

    def launchGroupMenu(self, name):
        self.clear()
        self.widgets["add-button"] = Button("+ Add FlashCard", 0.5, 0.2, 60, 1, self.window)
        self.widgets["add-button"].onClick(lambda: self.launchAddMenu())
