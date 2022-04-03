from unicodedata import name
from flask import Flask, render_template, url_for, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from server import authsession

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///asr.db'
db = SQLAlchemy(app)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup',methods=['GET','POST'])
def signup():
    return render_template('signup.html')
    
@app.route('/login',methods = ['POST', 'GET'])
def login():
    if 'username' in session:
        return redirect(url_for('dashboard',name = session["username"]))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/validate/<int:mode>',methods = ['POST', 'GET'])
def validate(mode):
    if request.method == 'POST':
        if request.form['username'] is not None and request.form['password'] is not None:
            if mode == 1:
                username = request.form['username']
                password = request.form['password']
                if authsession.validate_login(username,password) :
                    session['username'] = username
                    return redirect(url_for('dashboard',name = username))
                else:
                    return redirect(url_for('index'))
            elif mode == 0:
                username = request.form['username']
                password = request.form['password']
                if authsession.register(username,password) :
                    session['username'] = username
                    return redirect(url_for('dashboard',name = username))
        else:
            return redirect(url_for('index'))
    

@app.route('/dashboard/<name>')
def dashboard(name):
   return 'welcome %s' % name




if __name__ == "__main__":
    app.run(debug=True)