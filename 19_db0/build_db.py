# Chloe Wong, Tiffany Yang, Claire Song
# Team X
# SoftDev
# K19 -- All Your Database Are Belong To Us
# 2024-10-18
# Time Spent: 1

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
< < < INSERT YOUR TEAM'S DB-POPULATING CODE HERE > > >
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
#Creates a table using courses.csv
file = open("courses.csv", "r")
contents = csv.DictReader(file)
c.execute("CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)") #creates a table with code, mark, and id as the columns
for line in contents:
    value1 = line['code'] #assigns the data values in each row to 3 different variables
    value2 = line['mark']
    value3 = line['id']
    c.execute("INSERT INTO courses VALUES(?, ?, ?)", (value1, value2, value3)) #inserts data values from each row into the table

file = open("students.csv", "r") #creates another table the same way as before
contents = csv.DictReader(file)
c.execute("CREATE TABLE students(name TEXT, age INTEGER, id INTEGER)")
for line in contents:
    value1 = line['name']
    value2 = line['age']
    value3 = line['id']
    c.execute("INSERT INTO students VALUES(?, ?, ?)", (value1, value2, value3))

command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database