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


@app.context_processor
def inject_fake_user():
    return {
        'user': {'nickname': 'Me'},
        'current_year': date.today().year
    }


@app.route('/')
def index():
    return render_template(
        'index.html',
        title='Home',
    )


@app.route('/about/')
def about():
    return render_template(
        'base/base.html',
        title='Sign In',
    )


@app.route('/programs/')
def programs():
    return render_template(
        'base/base.html',
        title='Sign Up',
    )

