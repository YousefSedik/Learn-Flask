from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)

@app.route('/')
def home():
    if session.get('user'):
        pass
    
    return render_template('home.html')

@app.route('/login', methods=["POST", 'GET'])
def login():
    if request.method == "POST":
        print(request.form.get('name'))
        session['user'] = request.form.get('name')
        return redirect(url_for("home"))
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run()
    
