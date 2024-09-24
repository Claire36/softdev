# Claire Song
# SoftDev
# K09 -- Putting it Together
# 2024-09-23
# time spent: 0.5

# Changes Detected:
# Debug mode has now been turned on.
# When running, information about Debug mode is now presented at the bottom.
# Specfically, a PIN is provided as well as a line specifying that the debugger is running.
# Currently, our group has not found any substantial use for the PIN.
# Debug mode is used to update code in real-time (at least, in conjunction with the browser).


from flask import Flask
app = Flask(__name__)                 #create instance of class Flask

@app.route("/")                       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)                   #where will this go?
    return "No hablo queso!"

app.debug = True
app.run()