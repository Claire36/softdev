# Claire Song
# Novillo
# SoftDev
# K06 -- Divine your Destiny/Python File Handling/Get information from text files and return an entry weighted by a given percentage
# 2024-09-19
# time spent: 1.5

#DISCO: To pick a job class with the values next to them corresponding to the chance that the job class is picked, we can use csv.reader to turn each line in a csv file into a list of the job and the percentage, then add them to a big dictionary with the keys as the jobs and the values as the percentages. We can then take the list of keys and the list of values, then use random.choices and assign the list of values to be the weights.
#QCC: Would there be another way of choosing the job with the percentages as the weights without using random.choices and assigning a list of values to the weights parameter?
#How this script works: We create a dictionary with all the jobs as the keys and the percentages as the values by using csv.reader to find the job class and percentages in each line. We then create a list of the keys and values in the dictionary and use random.choice to pick a random value from the list of keys based on the percentages from the list of values.


import csv
import random

# function to read the CSV and return a dictionary of occupations and their percentages
def occupation_reader(file_path):
    occupations = {}
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)  # use csv.reader to handle quoted lines bc they exist in our file
        next(csv_reader)  # skip header
        for row in csv_reader:
            if len(row) == 2:  # check if we have exactly two elements (occupation, percentage)
                occupation = row[0].strip()
                percentage = float(row[1].strip())
                occupations[occupation] = percentage
    return occupations

# function to randomly select an occupation weighted by percentages
def weighted_rand(occupations):
    occupation_list = list(occupations.keys())
    weights = list(occupations.values())
    selected_occupation = random.choices(occupation_list, weights=weights, k=1)
    return selected_occupation[0]

if __name__ == "__main__":
    file_path = 'occupations.csv'
    occupations = occupation_reader(file_path)
    selected_occupation = weighted_rand(occupations)
    print(f"Random Occupation: {selected_occupation}")