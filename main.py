import tkinter
from MenuContainer import MenuContainer
from Menus import *

def launchProgram():
    # Launches the window application
    window = tkinter.Tk()
    window.title('Flashcard Application')

    # Sets the window dimensions
    window.geometry("800x600")
    window.minsize(800, 600)

    # Sets the background
    window.configure(background="black")

    # Launches and begins the loop for this entire application
    menu = MenuContainer(window)
    launchMainMenu(menu)

    window.mainloop()

launchProgram()