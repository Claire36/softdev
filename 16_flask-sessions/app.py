# Chloe Wong, Tiffany Yang, Claire Song
# Team X
# SoftDev
# K16 -- Take and Keep
# 2024-10-9
# Time Spent: 3

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session
import os

app = Flask(__name__)    #create Flask object
app.secret_key = os.urandom(32)

@app.route("/") #show login screen, shows response.html (home screen) if user is already logged in
def disp_loginpage():
    if 'username' in session:
        return render_template( 'response.html', response = session['username'], method = request.method)
    return render_template( 'login.html' )


@app.route("/auth", methods=['GET', 'POST']) #adds current username as an entry in session, then shows the hope page
def authenticate():
    session['username'] = request.args['username']
    return render_template( 'response.html', response = request.args['username'], method = request.method)  #response to a form submission

@app.route("/logout") #removes the username from session so that user can log out, then shows the logout screen
def logout():
    session.pop('username')
    return render_template( 'logout.html' )
    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()