"""
views
~~~~~

Specify options for Flask's development server.

:author: Sean Pianka
:e-mail: pianka@eml.cc

"""
from flask import render_template, request

from vulnbid import app


@app.context_processor
def inject_fake_user():
    return {
        'user': {'nickname': 'Me'}
    }


@app.route('/')
@app.route('/index/')
def index():
    return render_template(
        'index.html',
        title='Home',
        user=user
    )


@app.route('/testing/')
def testing():
    return render_template(
        'base/base.html',
        title='Home',
    )


@app.route('/signin/')
@app.route('/login/')
def signin():
    return render_template(
        'signin.html',
        title='Sign In',
    )


@app.route('/signup/')
@app.route('/register/')
def signup():
    return render_template(
        'signup.html',
        title='Sign Up',
    )
