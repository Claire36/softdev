# Claire Song
# Team X
# SoftDev
# K08 -- Learnination Via Deconstruction
# 2024-09-20
# time spent: 0.5

'''
DISCO:
__main__
127.0.0.1 - - [22/Sep/2024 18:00:17] "GET / HTTP/1.1" 200 -
is printed into the terminal every time we click on the link to the development server.

Clicking on the link leads us to a blank page with "No hablo queso!" printed on it. This is the return value of the hello_world() method.

This script can only be run from the terminal with the virtual environment activated, not from Thonny.

QCC:
0. When would it be appropriate to use a virtual environment?
1. __main__ seems to be printed in the terminal every time the server is accessed because print(__name__) is in the hello_world() method.
2. The flask module seems to be able to create web pages that display what you want it to.
3. The hello_world() method is called every time the server is accessed.
4. What does the @ symbol in front of the app.route("/") do?
5. How would we customize the web page further, besides giving it the words that we want it to show?
 ...

INVESTIGATIVE APPROACH:
We created a virtual environment and installed flask, then ran the script. We noticed that every time we refreshed the page or opened it up again, there would be something printed in the terminal. We concluded that this was because the hello_world() method was being run every time this was happening. We then looked closely at the method to see if we could discover anything about how the web page was made and messed around with the values that were printed and returned to see if we could find any patterns. We determined that the return value was shown on the screen, and the values that were printed showed up in the terminal.
'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs? We have seen similar syntax in Java, when creating instances of objects.

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'? The root directory is usually represented by '/'.
def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print? It prints to the terminal where the script is being run. It prints "__main__".
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know? This appears on the web page when we click on the link to the server. We saw this printed on the screen when we followed the link, and when we changed the values, the words on the screen changed along with it.

app.run()                                # Q5: Where have you seen similar constructs in other languages? We have seen similar constructs in java, when calling a method of a class using an object of that class.