# Claire Song
# Team X
# SoftDev
# K08 -- Learnination Via Deconstruction
# 2024-09-20
# time spent: 0.5

'''
DISCO:
<note any discoveries you made here... no m-atter how small!>

QCC:
0. Mainly java, C.
1. Your computer, the "root".
2. The root / your local host.
3. "No hablo queso!"
4. It appears on the local host interface. I know this because we tested it.
5. Java, the arrays attribute for length and how py is using .run().
 ...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs? Mainly java, C.
                                                    
@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'? Your computer, the "root".
def hello_world():
    print(__name__)                      # Q2: Where will this print to? The root / your local host.
                                         # Q3: What will it print? "No hable queso!"
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know? it.

app.run()                                # Q5: Where have you seen similar constructs in other languages?  you seen similar constructs in other languages? We have seen similar constructs in java, when calling a method of a class using an object of that class.