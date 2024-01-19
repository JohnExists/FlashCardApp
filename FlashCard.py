from datetime import datetime

class FlashCard:
    def __init__(self, front, back) -> None:
        self.front = front
        self.back = back
        self.sideDisplayed = 'F'
        self.status = "Unknown"
        now = datetime.now()
        self.date = now.strftime('%Y-%m-%d %H:%M:%S')

    def getDate(self):
        return self.date
    
    def get(self):
        if(self.sideDisplayed == 'F'): return self.front
        if(self.sideDisplayed == 'B'): return self.back

    def toggle(self):
        result = ""
        print(self.sideDisplayed)
        if(self.sideDisplayed == 'F'): 
            result = self.front
            self.sideDisplayed = 'B'
        elif(self.sideDisplayed == 'B'): 
            result = self.back
            self.sideDisplayed = 'F'

        return result
    
    def getStatus(self):
        return "Status: "+self.status+" (Click To Change)"
        
    def toggleStatus(self):
        result = ""
        if(self.status == "Unknown"):
            result = "Unknown"
            self.status = "Semi-Known"
        elif(self.status == "Semi-Known"):
            result = "Semi-Known"
            self.status = "Known"
        elif(self.status == "Known"):
            result = "Known"
            self.status = "Unknown"

        return "Status: "+result+" (Click To Change)"