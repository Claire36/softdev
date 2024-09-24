# Claire Song
# SoftDev
# K09 -- Putting it Together
# 2024-09-23
# time spent: 0.5

# Changes Detected:
# Comments are now added. Otherwise, the file is still the same.
# It does a good job of explaining the code, through being concise and to the point.

from flask import Flask
app = Flask(__name__)            #create instance of class Flask

@app.route("/")                  #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()