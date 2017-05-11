from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    username = StringField(
        'username',
        validators=[
            InputRequired("Enter your username.")
        ]
    )
    password = PasswordField(
        'password',
        validators=[
            InputRequired("Enter your password.")
        ]
    )
    remember_me = BooleanField(
        'remember_me'
    )
    submit = SubmitField(
        'Login'
    )


class RegisterForm(FlaskForm):
    username = StringField(
        'username',
        validators=[
            InputRequired("Enter your username.")
        ]
    )
    password = PasswordField(
        'password',
        validators=[
            InputRequired("Enter your password.")
        ]
    )
    submit = SubmitField(
        'login'
    )
