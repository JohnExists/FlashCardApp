from MenuContainer import *
from Button import Button
from FileManagement import *
from FlashGroup import FlashGroup

"""
Launches the main menu, allowing the user to
add a flashgroup or select a flashgroup

@param container The MenuContainer for which this menu is being held
"""
def launchMainMenu(container):
    container.clear()
    # Generates all components for the main menu

    # Initializes the buttons
    container.createButton("add-button", "+ Add", 0.5, 0.2, 60, 1)
    container.setButtonOnClick("add-button", lambda: launchAddCardGroupMenu(container))

    # Function called once the card group options are double clicked
    def onSelect(event):
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(selection[0])
        for group in container.flashGroups:
            if(group.getName() == value):
                launchCardGroupMenu(container, group)

    # Generates all the available flash groups strings
    flashGroupString = container.flashGroupsToString()
    container.generateLists("all-groups-list", flashGroupString)
    container.setListsOnDoubleClick("all-groups-list", onSelect)

"""
Launches the add group card that allows the user to
create a group of flashcards using a text box

@param container The MenuContainer for which this menu is being held
"""
def launchAddCardGroupMenu(container):
    container.clear()

    name = container.addVariable()
    container.generateEntry("name-entry", 0.2, name)
    
    def addGroup():
        if (name.get() != ""):
            container.flashGroups.append(FlashGroup(name.get()))
            addFlashgroupJSON(name.get())
            launchMainMenu(container)

    
    container.widgets["submit-button"] = Button("Add Group", 0.5, 0.5, 30, 3, container.window)
    container.widgets["submit-button"].onClick(lambda: addGroup())

    container.widgets["back-button"] = Button("Back", 0.5, 0.7, 30, 3, container.window)
    container.widgets["back-button"].onClick(lambda: launchMainMenu(container))


"""
Launches a flash group (group of flashcards),
allows the user to add a flashcards, edit a flashcard
or run the flashcards

@param container The MenuContainer for which this menu is being held
"""
def launchCardGroupMenu(container, flashGroup):
    container.clear()
    
    # Generates all components for the create flashcard menu
    container.createButton("run-button", "Run Flashcards", 0.5 , 0.15, 60, 1)
    container.createButton("add-button", "+ Add FlashCard", 0.5, 0.8, 60, 1)
    container.createButton("back-button", "Back", 0.5, 0.925, 60, 1)
    container.generateLists("flashcard-lists", flashGroup.strList())

    # Initializes all of these componenets
    container.setButtonOnClick("run-button", lambda: launchFlashcardMenu(container, flashGroup))
    container.setButtonOnClick("add-button", lambda: launchAddFlashCardMenu(container, flashGroup))
    container.setButtonOnClick("back-button", lambda: launchMainMenu(container))

    def onSelect(event):
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(selection[0])
        i = 1
        for flashcard in flashGroup.flashCards:
            if(value.find(f"Flashcard {i}") != -1):
                launchEditFlashcardMenu(container, flashGroup, flashcard)
            i += 1

    container.setListsOnDoubleClick("flashcard-lists", onSelect)

"""
Launches the add flashcard menu, allows the user
to create a flashcard using the front and the back

@param container The MenuContainer for which this menu is being held
"""
def launchAddFlashCardMenu(container, flashGroup):
    container.clear()

    # Generates all components for the create flashcard menu
    front, back = container.addVariable(), container.addVariable()
    container.generateEntry("front-entry", 0.2, front)
    container.generateEntry("back-entry", 0.3, back)
    container.createButton("submit-button", "Add FlashCard", 0.5, 0.5, 30, 3)
    container.createButton("back-button", "Back", 0.5, 0.7, 30, 3)

    def addFlashCard():
        flashcard = flashGroup.addFlashCard(front.get(), back.get(), "Unknown")
        addFlashcardJSON(flashGroup, flashcard)
        launchCardGroupMenu(container, flashGroup)

    # Initializes all of these componenets
    container.setButtonOnClick("back-button", lambda: launchCardGroupMenu(container, flashGroup))
    container.setButtonOnClick("submit-button", lambda: addFlashCard())


"""
Launches the edit flashcard menu, allows the user to
change the front and back of a pre-existing flashcard

@param container The MenuContainer for which this menu is being held
"""
def launchEditFlashcardMenu(container, flashGroup, flashcard):
    container.clear()

    front, back = container.addVariable(flashcard.front), container.addVariable(flashcard.back)
    container.generateEntry("front-entry", 0.2, front)
    container.generateEntry("back-entry", 0.3, back)
    container.createButton("edit-button", "Edit FlashCard", 0.5, 0.5, 40, 1)
    container.createButton("remove-button", "Remove Flashcard (Permanent)", 0.5, 0.6, 40, 1)
    container.createButton("back-button", "Back", 0.5, 0.7, 40, 1)


    def editFlashCard(front, back):
        flashcard.front = front
        flashcard.back = back
        flashcard.status = "Unknown"
        editFlashcardJSON(flashGroup, flashcard.date, front, back, "Unknown")
        launchCardGroupMenu(container, flashGroup)

    def removeFlashcard():
        flashGroup.flashCards.remove(flashcard)
        launchCardGroupMenu(container, flashGroup)
        deleteFlashcardJSON(flashGroup, flashcard.date)

    container.setButtonOnClick("edit-button", lambda: editFlashCard(front.get(), back.get()))
    container.setButtonOnClick("remove-button", lambda: removeFlashcard())
    container.setButtonOnClick("back-button", lambda: launchCardGroupMenu(container, flashGroup))


"""
Runs the group of flashcards, allows the user to test
themselves using each flashcard

@param container The MenuContainer for which this menu is being held
"""
def launchFlashcardMenu(container, flashGroup, index = 0):
    currentFlashCard = None
    if(index < 0 or index > len(flashGroup.flashCards) - 1): return
    currentFlashCard = flashGroup.getFlashCard(index)

    container.clear()

    currentFlashCard.sideDisplayed = 'F'

    # Generates all components for the run flashcard menu
    container.widgets["flashcard-button"] = Button(currentFlashCard.get(), 0.5, 0.3, 60, 12, container.window)
    container.widgets["prev-button"] = Button(">", 0.9, 0.3, 5, 12, container.window)
    container.widgets["next-button"] = Button("<", 0.1, 0.3, 5, 12, container.window)
    container.widgets["knowledge-level-button"] = Button(currentFlashCard.getStatus(), 0.5, 0.8, 60, 1, container.window)
    container.widgets["back-button"] = Button("Back To Flash Group Menu", 0.5, 0.9125, 60, 1, container.window)
    
    def toggleKnowledgeStatus():
        container.widgets["knowledge-level-button"].setText(currentFlashCard.toggleStatus())
        editFlashcardJSON(flashGroup, currentFlashCard.date, currentFlashCard.front, currentFlashCard.back,
                            currentFlashCard.status)

    # Initializes all of these componenets
    container.widgets["flashcard-button"].onClick(lambda: container.widgets["flashcard-button"].setText(currentFlashCard.toggle()))
    container.widgets["prev-button"].onClick(lambda: launchFlashcardMenu(container, flashGroup, index + 1))
    container.widgets["next-button"].onClick(lambda: launchFlashcardMenu(container, flashGroup, index - 1))
    container.widgets["knowledge-level-button"].onClick(lambda: toggleKnowledgeStatus())
    container.widgets["back-button"].onClick(lambda: launchCardGroupMenu(container, flashGroup))
