# Claire Song, Chloe Wong, Tiffany Yang
# Team X
# SoftDev
# K05 -- Bitstream/Python File Handling/Get information from text files and store it in a dictionary
# 2024-09-13
# time spent: 1

import random

dictList = []
file = open("krewess.txt", "r")

#split the data up so that each devo is a separate entry in a list
data = file.read().split("@@@")

#go through all the data and make a dictionary of the period, name, and duck for each devo and add all the dictionaries to a list 
for i in range(len(data) - 1):
    data[i] = data[i].split("$$$")
    dataDict = {"pd": data[i][0], "name": data[i][1], "duck": data[i][2]}
    dictList.append(dataDict)

#pick a random devo and print their information
index = random.randint(0, len(dictList) - 1)
entry = dictList[index]
print("Period: " + entry["pd"])
print("Name: " + entry["name"])
print("Ducky: " + entry["duck"])
