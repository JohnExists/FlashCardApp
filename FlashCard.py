from FileManagement import *

class FlashCard:
    """
    Initializes a new instance of the class.

    @param front The front text of this flashcard
    @param back The back text of this flashcard
    @param date The date that this flashcard was created
    @param status How well the user knows this flashcard (default: "Unknown")
    """
    def __init__(self, front, back, date, status = "Unknown") -> None:
        self.front = front
        self.back = back
        self.sideDisplayed = 'F'
        self.status = status
        self.date = date

    """
    @returns Gets the date that this flashcard was created
    """
    def getDate(self):
        return self.date
    
    """
    Gets the current side that this flashcard is facing (either front or back)

    @returns The text on the current side of this flashcard
    """
    def get(self):
        if(self.sideDisplayed == 'F'): return self.front
        if(self.sideDisplayed == 'B'): return self.back

    """
    Toggles which side of the flashcard is being displayed

    @returns The side that was displayed before the switch
    """
    def toggle(self):
        result = ""
        if(self.sideDisplayed == 'F'): 
            result = self.back
            self.sideDisplayed = 'B'
        elif(self.sideDisplayed == 'B'): 
            result = self.front
            self.sideDisplayed = 'F'

        return result

    def getStatus(self):
        return f"Status: {self.status} (Click To Change)"

    """
    Toggles between all 3 of the knowledge-statues for this specific
    flashcard (Unknown, Semi-known, Known)
    This allows the user to mark how well he can recall the card
    
    @returns The text for the current status that is displayed on the button
    """
    def toggleStatus(self):
        if(self.status == "Unknown"):
            self.status = "Semi-Known"
            return "Status: Semi-Known (Click To Change)"
        elif(self.status == "Semi-Known"):
            self.status = "Known"
            return "Status: Known (Click To Change)"
        elif(self.status == "Known"):
            self.status = "Unknown"
            return "Status: Unknown (Click To Change)"    