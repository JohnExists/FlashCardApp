import pygame


class Button:

    def __init__(self, x, y, width, height, txt):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.txt = txt
        self.isHovering = False
        self.onClick = lambda event: print("[GUIDE] Define onClick() function")
        self.clicked = False

        # create a font object.
        self.font = pygame.font.Font('freesansbold.ttf', 17)

        # create a text surface object,
        self.text = self.font.render(txt, True, (171, 32, 253))

        # create a rectangular object for the
        self.textRect = self.text.get_rect()

        # set the center of the rectangular object.
        self.textRect.center = (x + (width // 2), y + (height // 2))

    def setOnClick(self, onClick):
        self.onClick = onClick

    def draw(self, canvas):
        color = (171, 32, 253)
        if (self.isHovering): color = (255, 255, 255)
        pygame.draw.rect(canvas, color, [self.x, self.y, self.width, self.height], 2)
        canvas.blit(self.text, self.textRect)

    def hover(self, x, y):
        self.isHovering = ((self.x < x < self.x + self.width) and
                           (self.y < y < self.y + self.height))

    def click(self):
        if (self.isHovering):
            self.onClick(None)

