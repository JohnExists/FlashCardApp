from datetime import datetime

class FlashCard:
    def __init__(self, front, back) -> None:
        self.front = front
        self.back = back
        self.sideDisplayed = 'F'
        now = datetime.now()
        self.date = now.strftime('%Y-%m-%d %H:%M:%S')

    def getDate(self):
        return self.date