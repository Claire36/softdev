Chloe Wong, Tiffany Yang, Claire Song
Team X
SoftDev
K19 -- All Your Database Are Belong To Us
2024-10-18
Time Spent: 1

DISCOVERIES:
----------------------------------------------------
* You have to delete the database file every time you run the Python code because the table in the database cannot exist before you try to create it.
* When inserting values into tables, you have to use (?, ?, ?) in the string with the command, then specify the actual values later.
* When creating tables, you have to specify the data type of each of the columns you are creating.
====================================================


QUESTIONS/COMMENTS/CONCERNS:
----------------------------------------------------
Q: What exactly is the role of a cursor?
Q: How would you establish the relationship between two tables?
C: It seems to be pretty simple to execute many of the commands from the SQLite shell in Python by using cursor.execute(command), but commands such as .tables are exceptions.
====================================================