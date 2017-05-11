from flask import render_template

from vulnbid import app


@app.route('/')
def index():
    return render_template(
        'frontpage/index.html',
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

