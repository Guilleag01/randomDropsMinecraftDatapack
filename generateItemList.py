import os
import json 

def generateFromListOfFiles(path: str):
    itemList = list()
    
    generateBlocksAndEntities(os.path.join(path, "blocks"), itemList)
    generateBlocksAndEntities(os.path.join(path, "entities"), itemList)
    
    return itemList

def generateBlocksAndEntities(path: str, itemList: list):
    for filename in os.listdir(path):
        # There is a "sheep" folder, I ignore it
        if filename != "sheep":
            file = open(os.path.join(path, filename), "r")

            jsfile = dict()
            jsfile = json.load(file)

            # Check if that block of entity has any drops
            if "pools" in jsfile:
                for pool in jsfile["pools"]:
                    addItemsToList(pool["entries"], itemList)

# Recursively iterate over all drops or drop alternatives
def addItemsToList(lista: list, itemList: list):
    for x in lista:
        if x["type"] == "minecraft:item":

            # Add the found item to the list
            itemList.append(x["name"])
            
        if x["type"] == "minecraft:alternatives":
            addItemsToList(x["children"], itemList)