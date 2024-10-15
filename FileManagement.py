from FlashGroup import FlashGroup
import json

"""
Loads all the flashcards and group of flashcards
from the data.json file

@returns The list of all group of flashcards fully initiailized
"""
def loadData():
        f = open('data.json')
        data = json.load(f)
        
        result = []
        for i in data['flashgroups']:
            group = FlashGroup(i["name"])
            for j in i['flashcards']:
                  group.addFlashCard(j["front"], j["back"], j["knowledge"], j["date"])
            result.append(group)
        
        # Closing file
        f.close()
        return result

"""
Adds a new empty flashgroup into data.json file

@param newFlashgroupName The string name of this new flashgroup that is added
"""
def addFlashgroupJSON(newFlashgroupName):
        with open("data.json",'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside emp_details
            file_data["flashgroups"].append({"name": newFlashgroupName, "flashcards":[]})
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)

"""
Adds a new empty flashcard into data.json file

@param flashGroup The group that this flashcard is a part of
@param flashcard The new flashcard that is added into this flashgroup
"""
def addFlashcardJSON(flashGroup, flashcard):
        with open("data.json",'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)

            for flashgroupJSON in file_data["flashgroups"]:
                if flashgroupJSON["name"] != flashGroup.name: continue
                flashgroupJSON["flashcards"].append({"front": flashcard.front, "back": flashcard.back, 
                                                "knowledge" : "Unknown", "date": flashcard.date})
            
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)

"""
Changes the value of a pre-existing flashcard in the JSON file

@param flashGroup The flashgroup object that this flashcard is being contained in
@param date The date that this card was created, this value will be used to identify
which flashcard is being updated
@param front The new front text of this card
@param back The new back text of this card
@param status The new knowledge status of this card
"""
def editFlashcardJSON(flashGroup, date, front, back, status):
        with open("data.json",'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)

            for flashgroupJSON in file_data["flashgroups"]:
                if flashgroupJSON["name"] != flashGroup.name: continue
                for flashcardJSON in flashgroupJSON["flashcards"]:
                    if(flashcardJSON["date"] != date): continue
                    flashcardJSON["front"] = front
                    flashcardJSON["back"] = back
                    flashcardJSON["knowledge"] = status

            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)
            file.truncate()

def deleteFlashcardJSON(flashGroup, date):
        with open("data.json",'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)

            for flashgroupJSON in file_data["flashgroups"]:
                if flashgroupJSON["name"] != flashGroup.name: continue
                for i in range(len(flashgroupJSON["flashcards"])):
                    if(((flashgroupJSON["flashcards"])[i])["date"] != date): continue
                    del (flashgroupJSON["flashcards"])[i]

            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)
            file.truncate()
