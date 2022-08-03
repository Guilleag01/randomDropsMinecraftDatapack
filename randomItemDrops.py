import generateItemList as gil
import os
import json
import random



def main():
    path = os.path.join("data", "minecraft", "loot_tables")
    # path="data\\minecraft\\loot_tables"

    itemList = gil.generateFromListOfFiles("default")

    path1 = os.path.join(path, "blocks")
    path2 = os.path.join(path, "entities")

    # path1 = path + "\\blocks"
    # path2 = path + "\\entities"
    randLootTables(path1, itemList)
    randLootTables(path2, itemList)

def randLootTables(path: str, itemList: list):
    for filename in os.listdir(path):
        if filename != "sheep":
            file = open(os.path.join(path, filename), "r")
            # file = open(path + "\\" + filename, "r")
            jsfile = dict()
            jsfile = json.load(file)
            print(filename)

            if "pools" in jsfile:
                for pool in jsfile["pools"]:
                    randomize(pool["entries"], itemList)
            file.close()
            file = open(os.path.join(path, filename), "w")
            # file =  open(path + "\\" + filename, "w")
            json.dump(jsfile, file,indent=2)
            file.close()

def randomize(lista: list, itemList: list):
    for x in lista:
        if x["type"] == "minecraft:item":
            itemNum = random.randint(0, len(itemList) - 1)
            # print(str(itemNum) + " || " + str(len(itemList)))
            x["name"] = itemList[itemNum]
            itemList.remove(itemList[itemNum])

        if x["type"] == "minecraft:alternatives":
            randomize(x["children"], itemList)


if __name__ == "__main__":
    main()