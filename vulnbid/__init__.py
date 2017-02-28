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


from vulnbid import (
    models,
    forms,
    views,
)
