# Claire Song, Ben Rudinski
# Team Novillo
# SoftDev
# K06 -- Divine your Destiny/Python File Handling/Get information from text files and return an entry weighted by a given percentage
# 2024-09-19
# time spent: 1

import csv
import random

def occupation_reader(file_path): #function creating a dictionary from reading our csv
    occupations = {} #create dictionary
    with open(file_path, 'r') as file:
        next(file)
        for line in file:
            occupation, percentage = line.strip().split(',')
            occupations[occupation] = (float)(percentage)
    return occupations

def weighted_rand(occupations): #finds a weighted random choice from our dictionary
    occupation_list = list(occupations.keys())
    weights = list(occupations.values())
    selected_occupation = random.choices(occupation_list, weights, 1)
    return selected_occupation[0]

if __name__ == "__main__":
    file_path = "occupations.csv"
    occupations = occupation_reader(file_path)
    print(weighted_rand(occupations))