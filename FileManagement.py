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
        f = open('data.json')
        data = json.load(f)

        data['flashgroups'].append(newName)     