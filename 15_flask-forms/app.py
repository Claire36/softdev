'''
Claire Song
Topher Forever
SoftDev
K15 -- Take & Give
2024-10-08
time spent: 0.5
'''

from flask import Flask, render_template, request

app = Flask(__name__)

team_name = "Topher Forever"
roster = ["Ben Rudinski, Claire Song, Tiffany Yang"]

@app.route('/') #prompts user to log in
def index():
    return render_template('login.html', team_name=team_name, roster=roster)

@app.route('/submit', methods=['GET', 'POST']) #homepage shows the username & method & explanation
def submit():
    username = request.args.get('username') if request.method == 'GET' else request.form.get('username')
    method_used = request.method
    greeting = f"Hello, {username}! Welcome to our beautiful Flask App!"
    
    #explaining get vs post
    explanation = """
    GET: Sends data via the URL (useful for retrieving information).
    POST: Sends data through the body (useful for modifying server-side data).
    In this Flask app:
    - GET: The username is passed via the URL.
    - POST: The username is passed via the form body.
    """
    
    return render_template('response.html', username=username, method=method_used, greeting=greeting, explanation=explanation, team_name=team_name, roster=roster)

if __name__ == '__main__':
    app.run(debug=True)