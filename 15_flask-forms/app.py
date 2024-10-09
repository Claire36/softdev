'''
Claire Song
Team X
SoftDev
K15 -- Take & Give
2024-10-08
time spent: 0.5
'''

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

app = Flask(__name__)    #create Flask object


@app.route("/")
def disp_loginpage():
    return render_template( 'login.html' )

@app.route("/response", methods=['GET', 'POST']) # , methods=['GET', 'POST'])
def authenticate():
    return render_template('response.html', username=request.form['username'], method=request.method)

    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()