# Tiffany Yang, Chloe Wong, Claire Song
# Team X
# SoftDev
# K05 -- Adding more info to lists/dicts
# 2024-09-17
# time spent: 1 hour

import random

krewes_list = []  

def createList():
    with open("05_bitstream/krewes.txt", "r") as file:
        data = file.read().split("@@@")
        for person in data:
            info = person.split("$$$")
            krewes_list.append({"pd": info[0], "devo": info[1], "ducky": info[2]})

def pickDevo():
    createList()  
    if len(krewes_list) == 0:
        print("The list of krewes is empty!")
        return
    l = len(krewes_list) - 1
    choice = random.randint(0, l)
    devo = krewes_list[choice]
    print(devo["devo"] + " " + devo["pd"] + " " + devo["ducky"])

pickDevo()
