# Claire Song
# SoftDev
# K09 -- Putting it Together
# 2024-09-23
# time spent: 0.5

# Changes Detected:
# There is now a check to see if the file is running on the main module.
# Comments are also now in an informative state.
# Debug mode will only turn on if this is run on the main module.
# This is probably so that only the person writing and testing the code (i.e the only person who should be on the main module) can test their work.
# Other people (viewers; people who are not on the main module) will not see debug info.

from flask import Flask
app = Flask(__name__)           #create instance of class Flask

@app.route("/")                 #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":      # true if this file NOT imported
    app.debug = True            # enable auto-reload upon code change
    app.run()