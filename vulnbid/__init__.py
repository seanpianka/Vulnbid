"""
vulnbid
~~~~~~~

Specify options for Flask's development server.

:author: Sean Pianka
:e-mail: pianka@eml.cc

"""
from flask import Flask


app = Flask(__name__)
app.config.from_object('config')
app.config['TEMPLATES_AUTO_RELOAD'] = True


from vulnbid import (
    admin,
    auth,
    frontpage
)
