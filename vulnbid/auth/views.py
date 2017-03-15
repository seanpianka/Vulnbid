"""
views
~~~~~

Specify options for Flask's development server.

:author: Sean Pianka
:e-mail: pianka@eml.cc

"""
from datetime import date

from flask import render_template, request

from vulnbid import app


@app.route('/signin/')
@app.route('/login/')
def signin():
    return render_template(
        'base/base.html',
        title='Sign In',
    )


@app.route('/signup/')
@app.route('/register/')
def signup():
    return render_template(
        'base/base.html',
        title='Sign Up',
    )
