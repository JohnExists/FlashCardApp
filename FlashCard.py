import pygame


# Splits a large string into a list
def splitLargeString(word):
    if(' ' not in word): return [word]
    list = word.split(' ')

    wordsRow = ''
    result = []
    for word in list:
        wordsRow += word + " "
        if (len(wordsRow) > 22):
            result.append(wordsRow)
            wordsRow = ""
    return result


class FlashCard:
    def __init__(self, front, back):
        self.front = front
        self.back = back
        self.displayed = 'F'
        # create a font object.
        self.font = pygame.font.Font('freesansbold.ttf', 34)

        self.frontTxt = []
        for splitStr in splitLargeString(self.front):
            self.frontTxt.append(self.font.render(splitStr, True, (171, 32, 253)))

        self.backTxt = []
        for splitStr in splitLargeString(self.back):
            self.backTxt.append(self.font.render(splitStr, True, (171, 32, 253)))

    def draw(self, canvas):
        pygame.draw.rect(canvas, [171, 32, 253], [100, 150, 600, 400], 2)
        i = 0
        if (self.isDisplayingFront()):
            for txt in self.frontTxt:
                text_rect = txt.get_rect(center=(800 / 2, 600 / 2 + (50 * i)))
                canvas.blit(txt, text_rect)
                i += 1
        if (self.isDisplayingBack()):
            for txt in self.backTxt:
                text_rect = txt.get_rect(center=(800 / 2, 600 / 2 + (50 * i)))
                canvas.blit(txt, text_rect)
                i += 1

    def swap(self):
        if (self.isDisplayingFront()):
            self.displayed = 'B'
            return
        if (self.isDisplayingBack()):
            self.displayed = 'F'
            return

    def isDisplayingFront(self):
        return self.displayed == 'F'

    def isDisplayingBack(self):
        return self.displayed == 'B'

    def onClick(self, cursorX, cursorY):
        if((100 < cursorX < 700) and (150 < cursorY < 550)):
            self.swap()
