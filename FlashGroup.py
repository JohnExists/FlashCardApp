from FlashCard import FlashCard

class FlashGroup:

    def __init__(self, name) -> None:
        self.name = name
        self.flashCards = []

    def getName(self):
        return self.name

    def addFlashCard(self, front, back):
        self.flashCards.append(FlashCard(front, back))

    def getFlashCard(self, number):
        return self.flashCards[number]

    def strList(self):
        result = []
        i = 1
        for flashcard in self.flashCards:
            result.append(f"Flashcard {i}, Date: {flashcard.getDate()}")
            i += 1

        return result