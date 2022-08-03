import os
import json 

def generateFromListOfFiles(path: str):
    itemList = list()
    generateBlocksAndEntities(os.path.join(path, "blocks"), itemList)
    generateBlocksAndEntities(os.path.join(path, "entities"), itemList)
    print(len(itemList))
    return itemList

def generateBlocksAndEntities(path: str, itemList: list):
    
    for filename in os.listdir(path):
        if filename != "sheep":
            file = open(os.path.join(path, filename), "r")
            #file = open(path + "\\" + filename, "r")
            jsfile = dict()
            jsfile = json.load(file)

            if "pools" in jsfile:
                for pool in jsfile["pools"]:
                    addItemsToList(pool["entries"], itemList)

def addItemsToList(lista: list, itemList: list):
    for x in lista:
        if x["type"] == "minecraft:item":
            itemList.append(x["name"])
        if x["type"] == "minecraft:alternatives":
            addItemsToList(x["children"], itemList)