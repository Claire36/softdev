# Chloe Wong, Tiffany Yang, Claire Song
# Team X
# SoftDev
# K15 -- user sessions
# 2024-10-9
# Time Spent:

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session
import os

app = Flask(__name__)    #create Flask object
app.secret_key = os.urandom(32)

@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():
    #print("\n\n\n")
    #print("***DIAG: this Flask obj ***")
    #print(app)
    #print("***DIAG: request obj ***")
    #print(request)
    #print("***DIAG: request.args ***")
    #print(request.args)
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    #print("***DIAG: request.headers ***")
    #print(request.headers)
    if 'username' in session:
        return "Logged in as " + session['username']
    return render_template( 'login.html' )


@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    #print("\n\n\n")
    #print("***DIAG: this Flask obj ***")
    #print(app)
    #print("***DIAG: request obj ***")
    #print(request)
    #print("***DIAG: request.args ***")
    #print(request.args)
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    #print("***DIAG: request.headers ***")
    #print(request.headers)
    session['username'] = request.args['username']
    print(session)
    print(request.cookies)
    return render_template( 'response.html', response = request.args['username'], method = request.method)  #response to a form submission

@app.route("/logout")
def logout():
    session.pop('username')
    return render_template( 'logout.html' )
    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()