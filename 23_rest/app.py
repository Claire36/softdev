'''
Claire Song, Tracy Ye
CTV
SoftDev
K23 -- A RESTful Journey Skyward
2024-11-20
Time Spent: 1
'''

import urllib
import json
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def api():
    file = open("key_nasa.txt", "r")
    key = file.readlines()[0]
    with urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=' + key) as response:
        html = response.read()
        load = json.loads(html)
        #print(html)
        #print(load)
        #print(json.dumps(load))
    return render_template("main.html", source=load["url"], explanation=load["explanation"], source2=load["hdurl"])


if __name__ == "__main__":
    app.debug = True
    app.run()