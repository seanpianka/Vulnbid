from datetime import date

from flask import render_template, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required

from vulnbid import app
from vulnbid.forms import LoginForm
from vulnbid.utils import hash_password
from vulnbid.models import User


@app.route('/signin/')
@app.route('/login/')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit() and form.submit.data:
        username = str(form.username.data).strip()
        password = str(form.password.data).strip()
        remember_me = bool(form.remember_me.data)

        user = User.query.filter(User.username == username).first()

        if user and user.password == hash_password(password):
            login_user(user, remember=remember_me)
            return redirect(url_for('portal'))


    return render_template(
        'auth/login.html',
        form=form,
        title='Sign In',
    )


@app.route('/signout/')
@app.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/signup/')
@app.route('/register/')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    return render_template(
        'base/base.html',
        title='Sign Up',
    )
