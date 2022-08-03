import generateItemList as gil
import os
import json
import random

def main():
    path = os.path.join("data", "minecraft", "loot_tables")

    itemList = gil.generateFromListOfFiles("default")

    path1 = os.path.join(path, "blocks")
    path2 = os.path.join(path, "entities")

    randLootTables(path1, itemList)
    randLootTables(path2, itemList)

def randLootTables(path: str, itemList: list):
    for filename in os.listdir(path):
        # There is a "sheep" folder, I ignore it
        if filename != "sheep":
            file = open(os.path.join(path, filename), "r")

            jsfile = dict()
            jsfile = json.load(file)

            print(filename)

            # Check if that block of entity has any drops
            if "pools" in jsfile:
                for pool in jsfile["pools"]:
                    randomize(pool["entries"], itemList)

            file.close()
            file = open(os.path.join(path, filename), "w")

            json.dump(jsfile, file, indent=2)
            file.close()

# Recursively iterate over all drops or drop alternatives
def randomize(lista: list, itemList: list):
    for x in lista:
        if x["type"] == "minecraft:item":

            # Choose a random item from the item list and 
            # remove it from the item list
            item = random.choice(itemList)
            x["name"] = item
            itemList.remove(item)

        # If there is an alternative iterate over all the 
        # options of the alternative (recursive)
        if x["type"] == "minecraft:alternatives":
            randomize(x["children"], itemList)


if __name__ == "__main__":
    main()