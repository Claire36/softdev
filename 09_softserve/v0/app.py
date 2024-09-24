# Claire Song
# SoftDev
# K09 -- Putting it Together
# 2024-09-23
# time spent: 0.5

# Changes Detected:
# This file is the same as the app.py provided in work #08.
# The questions are replaced with comments that have nothing in them.
# This file fails to explain the code written.
# This is an example of a file that would not be efficient in catching others up to speed to your code.

from flask import Flask
app = Flask(__name__)          # ...

@app.route("/")                # ...
def hello_world():
    print(__name__)            # ...
    return "No hablo queso!"   # ...

app.run()                      # ...
                