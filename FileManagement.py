from FlashGroup import FlashGroup
import json

def loadData():
        f = open('data.json')
        data = json.load(f)
        
        result = []
        for i in data['flashgroups']:
            group = FlashGroup(i["name"])
            for j in i['flashcards']:
                  group.addFlashCard(j["front"], j["back"])
            result.append(group)
        
        # Closing file
        f.close()
        return result

def appendFlashGroupData(newName):

        with open("data.json",'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside emp_details
            file_data["flashgroups"].append({"name": newName, "flashcards":[]})
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)