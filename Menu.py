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
        self.widgets[name].configure(bg="black", fg="#ac20fd", width=25, font= ('Helvetica', 25), borderwidth = 0)
        self.widgets[name].pack()

        border_color.place(relx=0.5, rely=y, anchor="center")



    def launchMainMenu(self):
        self.clear()
        self.widgets["add-button"] = Button("+ Add", 0.2, 0.2, 20, 4, self.window)
        self.widgets["add-button"].onClick(lambda: self.launchAddMenu())

        i = 0
        for group in self.flashGroups:
            self.widgets[group] = Button(group, 0.5, 0.4 + (0.1 * i), 60, 1, self.window)
            self.widgets[group].alignText('w')
            i += 1

    def launchAddMenu(self):
        self.clear()

        name = self.addVariable()
        self.generateEntry("name-entry", 0.2, name)

        def addGroup():
            if(name.get() != ""):
                self.flashGroups.append(name.get())
                self.launchMainMenu()

        self.widgets["submit-button"] = Button("Add Group", 0.5, 0.5, 20, 4, self.window)
        self.widgets["submit-button"].onClick(lambda: addGroup())