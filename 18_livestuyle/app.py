# Chloe Wong, Tiffany Yang, Claire Song
# Team X
# SoftDev
# K18 -- Serving Looks
# 2024-10-16
# Time Spent: 1

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating

app = Flask(__name__)    #create Flask object

@app.route("/")
def mimic():
    return render_template("templates/index.html")

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()