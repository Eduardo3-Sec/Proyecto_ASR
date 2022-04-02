from unicodedata import name
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///asr.db'
db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup',methods=['GET','POST'])
def signup():
    return render_template('signup.html')
    
@app.route('/login',methods = ['POST', 'GET'])
def login():
    return render_template('login.html')

@app.route('/validate/<int:mode>',methods = ['POST', 'GET'])
def validate(mode):
    if request.method == 'POST':
        if mode == 1:
            if request.form['username'] is not None:
                user = request.form['username']
                return redirect(url_for('success',name = user))
            else:
                return redirect(url_for('index'))
        elif mode == 0:
            return redirect(url_for('success',name = user))
        else:
            return redirect(url_for('index'))
    

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

if __name__ == "__main__":
    app.run(debug=True)