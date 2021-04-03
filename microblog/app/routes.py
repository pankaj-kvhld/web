from app import app
from app.forms import LoginForm
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/login')
def login():
    form = LoginForm()
    return render_template("login.html", form=form)
