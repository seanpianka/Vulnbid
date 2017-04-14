"""
vulnbid/__init__.py
~~~~~~~~~~~~~~~~~~~

Specify options for Flask's development server.

:author: Sean Pianka
:e-mail: pianka@eml.cc

"""
from datetime import date

from flask import Flask
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object('config')

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'


@app.context_processor
def inject_fake_user():
    return {
        'user': {'nickname': 'Me'},
        'current_year': date.today().year
    }


from vulnbid import (
    admin,
    auth,
    frontpage
)
