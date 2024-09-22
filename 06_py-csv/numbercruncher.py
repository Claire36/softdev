# Claire Song, Ben Rudinski
# Team Novillo
# SoftDev
# K06 -- Divine your Destiny/Python File Handling/Get information from text files and return an entry weighted by a given percentage
# 2024-09-19
# time spent: 1

#DISCO: To pick a job class with the values next to them corresponding to the chance that the job class is picked, we can use csv.DictReader to turn each line in a csv file into a dictionary, then add them to a big dictionary with the keys as the jobs and the values as the percentages. We can then take the list of keys and the list of values, then use random.choice and assign the list of values to be the weights.
#QCC: Would there be another way of choosing the job with the percentages as the weights without using random.choice and assigning a list of values to the weights parameter?
#How this script works: We create a dictionary with all the jobs as the keys and the percentages as the values by using csv.DictReader to find the job class and percentages in each line. We then create a list of the keys and values in the dictionary and use random.choice to pick a random value from the list of keys based on the percentages from the list of values.

import csv
import random

def occupation_reader(file_path): #function creating a dictionary from reading our csv
    occupations = {} #create dictionary
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file) #each row is turned into a dictionary with its own values for Job Class and Percentage
        for line in reader:
            occupation, percentage = line['Job Class'], line['Percentage']
            occupations[occupation] = (float)(percentage) #add each row to the dictionary with the jobs as the keys and the numbers as the values
    return occupations

def weighted_rand(occupations): #finds a weighted random choice from our dictionary
    occupation_list = list(occupations.keys())
    occupation_list.remove("Total") #remove the last row from the list of occupations
    weights = list(occupations.values())
    weights.remove(99.8) #remove the last row from the list of weights
    selected_occupation = random.choices(occupation_list, weights, k=1)
    return selected_occupation[0]


file_path = "occupations.csv"
occupations = occupation_reader(file_path)
print(weighted_rand(occupations))
