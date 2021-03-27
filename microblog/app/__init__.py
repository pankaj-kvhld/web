from flask import Flask

app = Flask(__name__) # Flask is class because convention is that Class's first letter is capital. flask is either a package or module and contains the class Flask.

#Through this line one makes an object of Class Flask which is stored in object "app". for example if Flask is an abstract idea of apps then our microblog app is one specific app.

#convention is that you call the class as if it was a function and pass the information required to create an object. In this example one supplied the information __name__ to class Flask to create the object app.

from app import routes

# app is either a module or a package. Because we are importing. If there is a __init__.py file in a folder, then the rule (although an exception in latest versions of python, maybe) is that it is a package.

# hamne app naamak package se module routes.py ko amantrit karne ki koshish ki

"""
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
"""

# routes ne pahali line main hi app se app ko amantrit kiya parantu pahla app aur dusra app dono "not capital" hn arthat hum package se kuch import kar rahe hn arthat pahla app package h. jab yah package main __init.py__ main jaayega to dusri line main (code ki line no 3) app object mil jayega jo ki class Flask ka object h.

#arthat routes.py main jab bhi app object import karne ke baad saare app object ko denote kar rahe hn

# globals ka funda clear karna h
# word wrap alt z
# keyboard shortcuts ctrl ks searchable
# how to add screenshot