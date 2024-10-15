from FlashCard import FlashCard
from time import strftime, localtime
import time


class FlashGroup:
    """
    Initializes a new instance of the class.

    @param name The name of this group of flashcards
    """
    def __init__(self, name) -> None:
        self.name = name
        self.flashCards = []

    """
    @returns The unique name of this exact flash group object
    """
    def getName(self):
        return self.name

    """
    Creates a new flashcard and adds to the
    list of current flashcards in this group

    @param front The front text of the new flash card
    @param back The back text of the new flash card
    @param status The current status of knowledge of this flashcard
    @returns The new flashcard
    """
    def addFlashCard(self, front, back, status, date = int(time.time())):
        flashcard = FlashCard(front, back, date, status)
        self.flashCards.append(flashcard)
        return flashcard

    """
    @param number The index of the flashcard that needs to be
    obtained
    @returns The flashcard at that current index
    """
    def getFlashCard(self, number):
        return self.flashCards[number]

    """
    Converts the current list of flashcards into a list of
    strings, by labelling them as numbers and date

    @returns The list of strings for each flashcard
    """
    def strList(self):
        result = []
        i = 1
        for flashcard in self.flashCards:
            result.append(f"Flashcard {i}, Date: {strftime('%Y-%m-%d %H:%M:%S', localtime(flashcard.date))}")
            i += 1

        return result
    