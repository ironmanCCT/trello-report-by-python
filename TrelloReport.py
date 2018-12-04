import json
from pprint import pprint
#open the trello output JSON
fileName = 'trello-11-26.json'
with open(fileName, 'r', encoding="utf8") as f:
    data = json.load(f)
#close the original trello file.
f.close()
print("There are " + str(len(data["cards"]))+" cards in " + data["name"])
print("These are the lists and count of each card:")
uniqueIdList =[]
for card in data["cards"]:
##    print (card["idList"])
    ##if card["idList"] not in uniqueIdList:
    if  card["idList"] not in uniqueIdList:
        uniqueIdList.append(card["idList"])
##print(uniqueIdList)
##create a dictionary with idList: CountIdList
idListCount = {}
for list in uniqueIdList:
    idListCount[list] = 0
##pprint(idListCount)
for card in data["cards"]:
    idListCount[card["idList"]] += 1
with open("idListCount-"+fileName, "w", encoding="utf8") as file:
    file.write(json.dumps(idListCount))
file.close()
##pprint(idListCount)
##make a hash table with idList and name of list for easier reading
hashTable={}
for list in data["lists"]:
    ##pprint(list["name"]+" "+ list["id"])
    hashTable[list["id"]] = list["name"]

with open("hashtable-"+fileName, "w", encoding="utf8") as file:
    file.write(json.dumps(hashTable))
file.close()
##pprint(hashTable)
##print out the list name and number of cases from idListCount
for idList in idListCount:
    print("The number of cases in list "+hashTable[idList]+" : "+ str(idListCount[idList])+";")

##write report to file
with open("report-"+fileName+".txt", "w", encoding="utf8") as file:
    file.write(fileName+"\n")
    file.write("There are " + str(len(data["cards"]))+" cards in " + data["name"]+"\n")
    file.write("These are the lists and count of each card:\n")
    for idList in idListCount:
        file.write("The number of cases in list "+hashTable[idList]+" : "+ str(idListCount[idList])+";\n")
file.close()
