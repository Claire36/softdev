from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Blog model
class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)

# Entry model
class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)

@app.route('/')
def index():
    if 'username' in session:
        user = User.query.filter_by(username=session['username']).first()
        blogs = Blog.query.filter_by(user_id=user.id).all()
        return render_template('index.html', blogs=blogs)
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['username'] = user.username
            return redirect(url_for('index'))
        flash('Invalid username or password.')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/create_blog', methods=['GET', 'POST'])
def create_blog():
    if 'username' in session:
        if request.method == 'POST':
            title = request.form['title']
            user = User.query.filter_by(username=session['username']).first()
            new_blog = Blog(title=title, user_id=user.id)
            db.session.add(new_blog)
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('create_blog.html')
    return redirect(url_for('login'))

@app.route('/blog/<int:blog_id>')
def view_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    entries = Entry.query.filter_by(blog_id=blog.id).all()
    return render_template('view_blog.html', blog=blog, entries=entries)

@app.route('/add_entry/<int:blog_id>', methods=['GET', 'POST'])
def add_entry(blog_id):
    if 'username' in session:
        if request.method == 'POST':
            content = request.form['content']
            new_entry = Entry(content=content, blog_id=blog_id)
            db.session.add(new_entry)
            db.session.commit()
            return redirect(url_for('view_blog', blog_id=blog_id))
        return render_template('add_entry.html', blog_id=blog_id)
    return redirect(url_for('login'))

@app.route('/edit_entry/<int:entry_id>', methods=['GET', 'POST'])
def edit_entry(entry_id):
    entry = Entry.query.get_or_404(entry_id)
    if 'username' in session:
        if request.method == 'POST':
            entry.content = request.form['content']
            db.session.commit()
            return redirect(url_for('view_blog', blog_id=entry.blog_id))
        return render_template('edit_entry.html', entry=entry)
    return redirect(url_for('login'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
