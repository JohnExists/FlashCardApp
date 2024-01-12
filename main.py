import tkinter

from Menu import Menu

window = tkinter.Tk()

window.title('Flash Card Game')
window.geometry("800x600")
window.configure(background="black")

menu = Menu(window)

window.mainloop()