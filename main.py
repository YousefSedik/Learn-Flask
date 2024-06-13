from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.secret_key = "maybe-this-should-be-secret?"
app.permanent_session_lifetime = timedelta(minutes=5)

class Users(db.Model):
    _id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    email = db.Column('email', db.String(10))
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        

@app.route('/')
def home():
    name = None
    if session.get('user'):
        name = session.get('user')
        if request.method == 'POST':
            email = request.form.get('email')
            
    return render_template('home.html', name=name)

@app.route('/login', methods=["POST", 'GET'])
def login():
    if request.method == "POST":
        name = request.form.get('name')
        session['user'] = name
        found_user = Users.query.filter_by(name=name).first()
        if found_user:
            session['email'] = found_user.email
        else:
            usr = Users(name)
            db.session.add(use)
            db.session.commit()  
        return redirect(url_for("home"))
    
    elif session.get('user') is not None:
        return redirect(url_for('home'))
    
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    if session.get('user'):
        session.pop('user', None)
        session.pop('email', None)
        flash("You Just Logged out successfully! ")
    return redirect(url_for('login'))
    
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    
