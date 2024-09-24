# Claire Song
# SoftDev
# K09 -- Putting it Together
# 2024-09-23
# time spent: 0.5

# Changes Detected:
# A new comment has been added. This comment is not helpful at all, but it is safe to assume it was made in order to guide our insight as students.
# Running now prints "about to print __name__"..., where __name__ is __main__.
# This is because __main__ is the default name for a Python module.

from flask import Flask
app = Flask(__name__)             #create instance of class Flask

@app.route("/")                   #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)               #where will this go?
    return "No hablo queso!"

app.run()