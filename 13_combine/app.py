# Claire Song, Sasha Murokh
# we're cooking
# SoftDev
# K13 -- Template for Success
# 2024-09-30
# time spent: 1.5

import csv
import random
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def homepage():
    return "<a href='http://127.0.0.1:5000/wdywtbwygp'>link to jobs</a>"


@app.route("/wdywtbwygp") #shows table of possible jobs with a randomly selected job & its link
def occupations():
    occupations_table = []
    with open('data/occupations.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            item = [(row[0].strip()),(row[1].strip())]
            occupations_table.append(item) #adds info from occupations.csv into a 2d array with jobs and percentages
            
    occupations = {}
    with open('data/occupations.csv', mode='r') as file:
        csv_reader = csv.reader(file)  # use csv.reader to handle quoted lines bc they exist in our file
        next(csv_reader)  # skip header
        for row in csv_reader:
            if len(row) == 3:  # check if we have exactly three elements (occupation, percentage, link)
                occupation = row[0].strip()
                percentage = float(row[1].strip())
                occupations[occupation] = [percentage, row[2].strip()] #creates a dictionary with the job as the keys and the percentages and links as the values
    
    input_table = [(k, v[0]) for k, v in occupations.items()]
    input_table.insert(0,['Job Class','Percentage'])
    occupation_list = list(occupations.keys())
    weights = [value[0] for value in occupations.values()]
    selected_occupation = random.choices(occupation_list, weights=weights, k=1) #randomly selects an occupation based on the percentages
    return render_template('tablified.html', randomly_selected=selected_occupation[0], items=input_table, link=occupations[selected_occupation[0]][1])

if __name__ == "__main__":
    app.debug = True
    app.run()